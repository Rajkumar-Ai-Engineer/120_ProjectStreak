import Roboflow
import os
from ultralytics import YOLO
import supervision as sv
from supervision.draw.color import ColorPalette
from tqdm.notebook import tqdm
import cv2 as cv
import numpy as np
from collections import defaultdict, deque



class SpeedEstimator:

    def __init__(self,video_path="video.mp4",model_path="yolov8x.pt"):

        self.model = YOLO(model_path)
        self.ClassNames = self.model.model.names
        self.model_path = model_path
        self.video_path = video_path
        self.target_path = "result.mp4"
        self.video_info = sv.VideoInfo.from_video_path(self.video_path)
        self.byte_tracker = sv.ByteTrack(frame_rate=self.video_info.fps)
        self.thickness =  sv.calculate_optimal_line_thickness(
            resolution_wh=self.video_info.resolution_wh
        )
        self.BBoxAnnotator = sv.BoundingBoxAnnotator(thickness=self.thickness)
        self.label_annotator = sv.LabelAnnotator(
            text_scale=2,
            text_thickness=4,
            text_position=sv.Position.BOTTOM_CENTER
        )

        self.trace_annotator = sv.TraceAnnotator(
            thickness=self.thickness,
            trace_length=self.video_info.fps * 2,
            position=sv.Position.BOTTOM_CENTER
        )

        self.MODEL_RESOLUTION = 1280
        self.confidence_thres = 0.3
        self.iou_thres = 0.5
        self.Source = np.array([
                        [1252, 787],
                        [2298, 803],
                        [5039, 2159],
                        [-550, 2159]
                        ]).astype(np.float32)
        self.target_Width = 25
        self.target_height = 250
        self.target = np.array([
                    [0,0],
                    [self.target_Width - 1,0],
                    [self.target_Width - 1,self.target_height - 1],
                    [0,self.target_height - 1]
                ]).astype(np.float32)
        self.matrix = cv.getPerspectiveTransform(self.Source,self.target)
        self.frame_generator = sv.get_video_frames_generator(self.Source)

    def transform_points_views(self,points):
        if points.size == 0:
            return points

        reshaped_points = points.reshape(-1,1,2)
        transformed_points = cv.perspectiveTransform(reshaped_points, self.matrix)
        return transformed_points.reshape(-1, 2)

    def video_save(self):
        polygon_zone = sv.PolygonZone(polygon=self.Source)
        coordinates = defaultdict(lambda: deque(maxlen=self.video_info.fps))

        with sv.VideoSink(self.target_path, self.video_info) as sink:
            # Loop over frames in the source video
            for frame in tqdm(self.frame_generator, total=self.video_info.total_frames):
                # Run the YOLO model on the current frame
                result = self.model(frame, imgsz=self.MODEL_RESOLUTION , verbose=False)[0]
                detections = sv.Detections.from_ultralytics(result)

                # Filter detections by confidence and class
                detections = detections[detections.confidence > self.confidence_thres]
                detections = detections[detections.class_id != 0]

                # Draw the polygon on the frame (not detections)
                annotated_frame = frame.copy()
                annotated_frame = sv.draw_polygon(
                    scene=annotated_frame,
                    polygon=self.Source,
                    color=sv.Color(255, 0, 0),
                    thickness=4
                )

                # Filter detections inside the polygon zone
                detections = detections[polygon_zone.trigger(detections)]

                # Apply non-max suppression to refine detections
                detections = detections.with_nms(self.iou_thres)

                # Track detections
                detections = self.byte_tracker.update_with_detections(detections=detections)

                # Get anchor coordinates for speed calculation
                points = detections.get_anchors_coordinates(
                    anchor=sv.Position.BOTTOM_CENTER
                )
                points = self.transform_points_views(points=points).astype(int)

                # Store detections' positions
                for tracker_id, [_, y] in zip(detections.tracker_id, points):
                    coordinates[tracker_id].append(y)

                # Generate labels with speed if enough data is available
                labels = []
                for tracker_id in detections.tracker_id:
                    if len(coordinates[tracker_id]) < self.video_info.fps / 2:
                        labels.append(f"#{tracker_id}")
                    else:
                        coordinate_start = coordinates[tracker_id][-1]
                        coordinate_end = coordinates[tracker_id][0]
                        distance = abs(coordinate_start - coordinate_end)
                        time = len(coordinates[tracker_id]) / self.video_info.fps
                        speed = distance / time * 3.6  # Convert to km/h
                        labels.append(f"#{tracker_id} {int(speed)} km/h")

                # Annotate the frame with traces, boxes, and labels
                annotated_frame = self.trace_annotator.annotate(
                    scene=annotated_frame, detections=detections
                )
                annotated_frame = self.BBoxAnnotator.annotate(
                    scene=annotated_frame, detections=detections
                )
                annotated_frame = self.label_annotator.annotate(
                    scene=annotated_frame, detections=detections, labels=labels
                )

                # Write the annotated frame to the target video
                sink.write_frame(annotated_frame)

