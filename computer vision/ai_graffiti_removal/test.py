import os
import cv2 as cv

import cv2
import numpy as np
import random
from matplotlib import pyplot as plt


def create_synthetic_graffiti(image_path, output_path):
    """Create a synthetic graffiti image for demonstration"""
    # Load the original image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found")

    # Create a copy to draw graffiti on
    graffiti_img = img.copy()
    height, width = img.shape[:2]

    # Draw random graffiti-like elements
    colors = [
        (255, 0, 0),  # Red
        (0, 255, 0),  # Green
        (0, 0, 255),  # Blue
        (255, 255, 0),  # Yellow
        (255, 0, 255),  # Magenta
        (0, 255, 255),  # Cyan
    ]

    # Draw random text
    for _ in range(3):
        text = "GRAFFITI"
        font = random.choice([
            cv2.FONT_HERSHEY_SIMPLEX,
            cv2.FONT_HERSHEY_COMPLEX,
            cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        ])
        pos = (random.randint(50, width - 200), random.randint(50, height - 50))
        scale = random.uniform(0.8, 2.5)
        color = random.choice(colors)
        thickness = random.randint(2, 5)

        cv2.putText(graffiti_img, text, pos, font, scale, color, thickness, cv2.LINE_AA)

    # Draw random shapes
    for _ in range(5):
        pt1 = (random.randint(0, width), random.randint(0, height))
        pt2 = (random.randint(0, width), random.randint(0, height))
        color = random.choice(colors)
        thickness = random.randint(1, 3)
        cv2.line(graffiti_img, pt1, pt2, color, thickness)

    for _ in range(3):
        center = (random.randint(0, width), random.randint(0, height))
        radius = random.randint(10, 50)
        color = random.choice(colors)
        thickness = random.choice([-1, 1, 2, 3])
        cv2.circle(graffiti_img, center, radius, color, thickness)

    # Save the result
    cv2.imwrite(output_path, graffiti_img)
    return graffiti_img


def create_mask_interactive(image):
    """Create a mask by letting the user draw on the image"""
    clone = image.copy()
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    drawing = False

    def mouse_callback(event, x, y, flags, param):
        nonlocal drawing, clone, mask

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            cv2.circle(mask, (x, y), 5, 255, -1)
            cv2.circle(clone, (x, y), 5, (0, 0, 255), -1)

        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                cv2.circle(mask, (x, y), 5, 255, -1)
                cv2.circle(clone, (x, y), 5, (0, 0, 255), -1)

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False

    cv2.namedWindow("Mark Graffiti (Press 'd' when done)")
    cv2.setMouseCallback("Mark Graffiti (Press 'd' when done)", mouse_callback)

    while True:
        cv2.imshow("Mark Graffiti (Press 'd' when done)", clone)
        key = cv2.waitKey(1) & 0xFF

        # Press 'r' to reset
        if key == ord("r"):
            clone = image.copy()
            mask = np.zeros(image.shape[:2], dtype=np.uint8)
        # Press 'd' when done
        elif key == ord("d"):
            break

    cv2.destroyAllWindows()
    return mask


def remove_graffiti(image, mask, method='telea'):
    """Remove graffiti using specified inpainting method"""
    if method == 'telea':
        return cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
    elif method == 'ns':
        return cv2.inpaint(image, mask, 3, cv2.INPAINT_NS)
    else:
        raise ValueError("Unknown method. Use 'telea' or 'ns'")


def compare_methods(image, mask):
    """Compare both inpainting methods"""
    result_telea = remove_graffiti(image, mask, 'telea')
    result_ns = remove_graffiti(image, mask, 'ns')

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original with Graffiti")
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(mask, cmap='gray')
    plt.title("Mask")
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(result_telea, cv2.COLOR_BGR2RGB))
    plt.title("Telea Method")
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(cv2.cvtColor(result_ns, cv2.COLOR_BGR2RGB))
    plt.title("Navier-Stokes Method")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    return result_telea, result_ns


def main():
    # Step 1: Create synthetic graffiti (or use your own image)
    input_image = "original.png"  # Replace with your image
    graffiti_image = "graffiti_image.jpg"
    result_image = "cleaned_image.jpg"

    # Create synthetic graffiti (skip if you have your own graffiti image)
    print("Creating synthetic graffiti for demonstration...")
    graffiti_img = create_synthetic_graffiti(input_image, graffiti_image)

    # Step 2: Create mask interactively
    print("\nInteractive mask creation:")
    print("1. Use mouse to mark graffiti areas (left click and drag)")
    print("2. Press 'r' to reset the mask")
    print("3. Press 'd' when done marking")
    mask = create_mask_interactive(graffiti_img)

    # Step 3: Remove graffiti and compare methods
    print("\nProcessing image...")
    result_telea, result_ns = compare_methods(graffiti_img, mask)

    # Save the results
    cv2.imwrite("result_telea.jpg", result_telea)
    cv2.imwrite("result_ns.jpg", result_ns)
    print(f"\nResults saved as 'result_telea.jpg' and 'result_ns.jpg'")


if __name__ == "__main__":
    main()

