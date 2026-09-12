
import cv2
import numpy as np


def calculate_statistics(original_image, edge_image):
    """Calculate basic image and edge statistics."""
    height, width = original_image.shape[:2]

    total_pixels = edge_image.size
    edge_pixels = np.count_nonzero(edge_image)

    edge_percentage = (edge_pixels / total_pixels) * 100

    return {
        "width": width,
        "height": height,
        "channels": (
            original_image.shape[2]
            if len(original_image.shape) == 3
            else 1
        ),
        "edge_pixels": int(edge_pixels),
        "edge_percentage": round(edge_percentage, 2)
    }