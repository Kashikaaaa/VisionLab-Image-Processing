
import cv2


def convert_to_grayscale(image):
    """Convert a color image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_gaussian_blur(gray_image, kernel_size=5):
    """Reduce image noise using Gaussian blur."""
    return cv2.GaussianBlur(
        gray_image,
        (kernel_size, kernel_size),
        0
    )