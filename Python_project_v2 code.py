import cv2
import numpy as np


def count_rbc_cells(image_path):
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Image not found at '{image_path}'")
        return None, None

    output = image.copy()

    # Remove the light border region to avoid false detections
    crop_margin = 10
    cropped = image[crop_margin:-crop_margin, crop_margin:-crop_margin]

    # Convert to grayscale
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

    # Smooth image
    blur = cv2.medianBlur(gray, 5)

    # Hough Circle detection tuned for RBC-like cells
    circles = cv2.HoughCircles(
        blur,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=16,
        param1=60,
        param2=15,
        minRadius=8,
        maxRadius=18
    )

    cell_count = 0

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            # Shift coordinates back to original image
            x_full = x + crop_margin
            y_full = y + crop_margin

            cv2.circle(output, (x_full, y_full), r, (0, 255, 0), 2)
            cv2.circle(output, (x_full, y_full), 2, (0, 0, 255), 3)
            cell_count += 1

    return cell_count, output


if __name__ == "__main__":
    IMAGE_PATH = "image.png"   # replace with your image file name

    count, result_image = count_rbc_cells(IMAGE_PATH)

    if count is not None:
        print("Estimated RBC Count:", count)

        cv2.imshow("Detected RBCs", result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
