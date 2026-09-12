# VisionLab: Image Processing and Edge Detection Studio

## 1. Project Overview

VisionLab is an interactive image-processing application developed using Python, OpenCV, NumPy, Pillow, and Streamlit.

The project allows users to upload an image and apply various image-processing techniques. It provides a simple interface for viewing the original image, processed images, and basic image statistics.

The main purpose of this project is to demonstrate fundamental image-processing and edge-detection operations through an easy-to-use application.

## 2. Features

* Upload an image through the Streamlit interface.
* Display the original image.
* Convert an image to grayscale.
* Apply Gaussian blur for noise reduction.
* Detect edges using the Canny Edge Detection algorithm.
* Apply binary thresholding.
* Display basic image statistics.
* Download processed images.
* Provide an interactive and user-friendly interface.

## 3. Technologies and Tools Used

* **Python** – Main programming language.
* **OpenCV** – Image processing and edge detection.
* **NumPy** – Numerical and array operations.
* **Pillow** – Image handling.
* **Streamlit** – Web-based interactive user interface.
* **Git and GitHub** – Version control and project hosting.
* **Visual Studio Code** – Development environment.

## 4. Project Structure

```text
VisionLab-Image-Processing/
│
├── app.py
├── analysis.py
├── edge_detection.py
├── preprocessing.py
├── requirements.txt
├── README.md
├── statement.md
├── .gitignore
└── venv/
```

## 5. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Kashikaaaa/VisionLab-Image-Processing.git
```

### Step 2: Open the Project Directory

```bash
cd VisionLab-Image-Processing
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Required Packages

```bash
pip install -r requirements.txt
```

## 6. Running the Project

Run the following command in the terminal:

```bash
streamlit run app.py
```

The application will open in a web browser. If it does not open automatically, copy the local URL displayed in the terminal and open it in your browser.

## 7. Instructions for Testing

1. Start the application using the command given above.
2. Upload a valid image file through the Streamlit interface.
3. Check whether the original image is displayed correctly.
4. Verify the grayscale image output.
5. Verify that Gaussian blur is applied.
6. Check whether edges are detected using the Canny Edge Detection algorithm.
7. Verify the binary threshold output.
8. Check the displayed image statistics.
9. Click the download buttons and verify that the processed images can be downloaded.
10. Test the application with different image sizes and image formats.

## 8. Expected Result

After uploading an image, the application should display the original image along with its processed versions, including the grayscale image, Gaussian-blurred image, Canny edge-detected image, and binary threshold image.

The user should also be able to view basic image statistics and download the processed images.

## 9. Screenshots

### Main Application Interface

![Main Application Interface](screenshots/1.png)

### Image Processing Results

![Image Processing Results](screenshots/2.png)
