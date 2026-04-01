import cv2
import numpy as np

def count_cells(image_path):
    # Step 1: Load image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Image not found at '{image_path}'")
        return None, None

    # Step 2: Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 3: Noise removal
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 4: Adaptive threshold
    thresh = cv2.adaptiveThreshold(
        blur, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11, 2
    )

    # Step 5: Remove noise using morphology
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Step 6: Sure background
    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    # Step 7: Distance transform
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

    # Step 8: Sure foreground
    _, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)

    # Step 9: Unknown region
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Step 10: Marker labelling
    _, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0

    # Step 11: Apply Watershed
    markers = cv2.watershed(image, markers)

    # Step 12: Count cells (ignore background -1 boundaries and label 1 background)
    cell_count = len(np.unique(markers)) - 2

    # Step 13: Draw boundaries in red
    result = image.copy()
    result[markers == -1] = [0, 0, 255]

    return cell_count, result


if __name__ == "__main__":
    IMAGE_PATH = "cells.jpg"

    count, result_image = count_cells(IMAGE_PATH)

    if count is not None:
        print(f"Accurate Cell Count: {count}")
        cv2.imshow("Cell Detection Result", result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
