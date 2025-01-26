#  Face Extraction 

This script extracts faces from an image using OpenCV's Haar cascade for face detection and saves them as individual image files.

## Prerequisites

1. **Python Installation**:
   - Ensure you have Python 3.x installed on your system.

2. **Required Libraries**:
   - OpenCV
   - To install OpenCV, run the following command:
     ```bash
     pip install opencv-python
     ```

3. **Files Needed**:
   - An image file (e.g., `Face.jpg`) containing faces to extract.
   - Haar cascade XML file for face detection (e.g., `haarcascade_frontalface_default.xml`).
     - Download [haarcascade_frontalface_default.xml model](https://drive.google.com/file/d/1-Q1T9ds4z-1j3hQxl0D95PKVFk-Y7rnD/view?usp=sharing).

## How to Use

1. Place the image (`Face.jpg`) and the Haar cascade file (`haarcascade_frontalface_default.xml`) in the same directory as the script.

2. Run the script:
   ```bash
   python app.py
   ```

3. The script will:
   - Detect faces in the image.
   - Save each detected face as a separate image in the `Extract_Faces_From_Image/Faces` directory.

4. Check the `Extract_Faces_From_Image/Faces` folder for the extracted face images.

## Code Explanation

### 1. Import Required Libraries
```python
import cv2
import os
```

### 2. Define Paths
Ensure the image file and Haar cascade XML file paths are correct:
```python
image_path = 'Face.jpg'
haarcascade_path = 'haarcascade_frontalface_default.xml'
```

### 3. Check File Existence
Validate that the necessary files exist:
```python
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image file '{image_path}' not found.")
if not os.path.exists(haarcascade_path):
    raise FileNotFoundError(f"Haar cascade file '{haarcascade_path}' not found.")
```

### 4. Detect Faces
Detect faces using the Haar cascade:
```python
faces = faceCascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4)
```

### 5. Save Detected Faces
Save each detected face as a separate image in the specified directory:
```python
output_dir = os.path.join(os.getcwd(), 'Extract_Faces_From_Image', 'Faces')
os.makedirs(output_dir, exist_ok=True)
```

## Output
The script creates a directory `Extract_Faces_From_Image/Faces` and saves each detected face as `Face1.jpg`, `Face2.jpg`, and so on.


## Troubleshooting

1. **No Faces Detected**:
   - Ensure the image contains visible faces.
   - Check lighting and image quality.

2. **Haar Cascade Not Found**:
   - Ensure the Haar cascade XML file is in the correct path.

3. **Output Directory Not Created**:
   - Check file permissions for the script's directory.

