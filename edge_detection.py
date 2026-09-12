
import cv2


def detect_edges(gray_image, lower_threshold=50, upper_threshold=150):
    """Detect edges using the Canny algorithm."""
    return cv2.Canny(
        gray_image,
        lower_threshold,
        upper_threshold
    )


def apply_threshold(gray_image, threshold_value=127):
    """Convert a grayscale image into a binary image."""
    _, binary_image = cv2.threshold(
        gray_image,
        threshold_value,
        255,
        cv2.THRESH_BINARY
    )

    return binary_image