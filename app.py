import cv2
import numpy as np
import streamlit as st
from PIL import Image

from preprocessing import (
    convert_to_grayscale,
    apply_gaussian_blur
)

from edge_detection import (
    detect_edges,
    apply_threshold
)

from analysis import calculate_statistics


st.set_page_config(
    page_title="VisionLab",
    page_icon="🖼️",
    layout="wide"
)


st.title("VisionLab")

st.subheader("Image Processing and Edge Detection Studio")

st.write(
    "Upload an image and explore common Computer Vision "
    "techniques using OpenCV."
)


uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    try:
        # Read uploaded image
        pil_image = Image.open(uploaded_file).convert("RGB")

        image_rgb = np.array(pil_image)

        image_bgr = cv2.cvtColor(
            image_rgb,
            cv2.COLOR_RGB2BGR
        )

        # Convert image to grayscale
        gray_image = convert_to_grayscale(image_bgr)

        # Sidebar controls
        blur_kernel = st.sidebar.slider(
            "Gaussian blur kernel size",
            min_value=1,
            max_value=15,
            value=5,
            step=2
        )

        lower_threshold = st.sidebar.slider(
            "Lower Canny threshold",
            0,
            255,
            50
        )

        upper_threshold = st.sidebar.slider(
            "Upper Canny threshold",
            0,
            255,
            150
        )

        binary_threshold = st.sidebar.slider(
            "Binary threshold",
            0,
            255,
            127
        )

        # Apply image processing
        blurred_image = apply_gaussian_blur(
            gray_image,
            blur_kernel
        )

        edge_image = detect_edges(
            blurred_image,
            lower_threshold,
            upper_threshold
        )

        binary_image = apply_threshold(
            gray_image,
            binary_threshold
        )

        # Calculate image statistics
        statistics = calculate_statistics(
            image_bgr,
            edge_image
        )

        st.header("Processing Results")

        # Original and grayscale images
        col1, col2 = st.columns(2)

        with col1:
            st.image(
                image_rgb,
                caption="Original Image",
                use_column_width=True
            )

        with col2:
            st.image(
                gray_image,
                caption="Grayscale Image",
                use_column_width=True
            )

            gray_bytes = cv2.imencode(
                ".png",
                gray_image
            )[1].tobytes()

            st.download_button(
                label="⬇️ Download Grayscale Image",
                data=gray_bytes,
                file_name="grayscale.png",
                mime="image/png",
                key="gray_download"
            )

        # Blurred and edge images
        col3, col4 = st.columns(2)

        with col3:
            st.image(
                blurred_image,
                caption="Gaussian Blurred Image",
                use_column_width=True
            )

            blurred_bytes = cv2.imencode(
                ".png",
                blurred_image
            )[1].tobytes()

            st.download_button(
                label="⬇️ Download Blurred Image",
                data=blurred_bytes,
                file_name="blurred.png",
                mime="image/png",
                key="blurred_download"
            )

        with col4:
            st.image(
                edge_image,
                caption="Canny Edge Detection",
                use_column_width=True
            )

            edge_bytes = cv2.imencode(
                ".png",
                edge_image
            )[1].tobytes()

            st.download_button(
                label="⬇️ Download Edge Image",
                data=edge_bytes,
                file_name="canny_edges.png",
                mime="image/png",
                key="edge_download"
            )

        # Binary thresholding
        st.subheader("Binary Thresholding")

        st.image(
            binary_image,
            caption="Binary Threshold Image",
            use_column_width=True
        )

        binary_bytes = cv2.imencode(
            ".png",
            binary_image
        )[1].tobytes()

        st.download_button(
            label="⬇️ Download Binary Image",
            data=binary_bytes,
            file_name="binary_threshold.png",
            mime="image/png",
            key="binary_download"
        )

        # Image statistics
        st.subheader("Image Statistics")

        stat1, stat2, stat3, stat4 = st.columns(4)

        stat1.metric(
            "Width",
            statistics["width"]
        )

        stat2.metric(
            "Height",
            statistics["height"]
        )

        stat3.metric(
            "Edge Pixels",
            statistics["edge_pixels"]
        )

        stat4.metric(
            "Edge Percentage",
            f'{statistics["edge_percentage"]}%'
        )

    except Exception as error:
        st.error(
            f"Unable to process this image. Error: {error}"
        )

else:
    st.info("Please upload an image to begin.")