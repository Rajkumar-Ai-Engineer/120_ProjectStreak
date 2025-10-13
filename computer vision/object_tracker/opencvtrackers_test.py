import cv2 as cv
import sys

def select_tracker(tracker_type: str):
    if tracker_type == "BOOSTING":
        return cv.legacy.TrackerBoosting_create()
    elif tracker_type == "MIL":
        return cv.legacy.TrackerMIL_create()
    elif tracker_type == "KCF":
        return cv.legacy.TrackerKCF_create()

def main():
    trackers = ["BOOSTING", "MIL", "KCF"]  
    print("Select the tracker type!")
    for i, tracker in enumerate(trackers):
        print(f"{i}: {tracker}")
        
    tracker_choice = int(input("Enter tracker Number:"))
    tracker_type = trackers[tracker_choice]
    tracker = select_tracker(tracker_type=tracker_type)
    
    video_path = input("Enter video file path:")
    
    if not video_path:
        cam = cv.VideoCapture(0)
    else:
        cam = cv.VideoCapture(video_path)
    
    ok, frame = cam.read()
        
    bbox = cv.selectROI(frame, False)    
    ok = tracker.init(frame, bbox)
    
    while True:
        ok, frame = cam.read()
        
        if not ok:
            break 
        
        ok,bbox = tracker.update(frame)
        
        if ok:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))  # Fixed bounding box calculation
            cv.rectangle(frame, p1, p2, (0, 255, 0), 2)
        else:
            cv.putText(frame, "Tracker failed to execute", (100, 20), cv.FONT_HERSHEY_SIMPLEX, 0.25, (0, 0, 255), 2)
        
        cv.putText(frame, tracker_type + " Tracker", (100, 20),cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv.putText(frame, "ESC to quit", (100, 50),cv.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 2)
        
        cv.imshow("frame", frame)
        
        if cv.waitKey(1) & 0xFF == 27:  # ESC key to quit
            break
        
    cam.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
