# Face Alignment Using Dlib and OpenCV

This project aligns a face in an image by detecting facial landmarks, calculating the tilt angle, and rotating the image to make the face upright. The program is built using Python, OpenCV, and Dlib's facial landmark detection model.

---

## Features

- **Face Detection:** Uses Dlib's pre-trained frontal face detector to locate faces in an image.
- **Facial Landmark Detection:** Identifies 68 key facial landmarks with a focus on the nose bridge and nose tip.
- **Angle Calculation:** Calculates the tilt angle of the face using trigonometric functions.
- **Image Alignment:** Rotates the image to ensure the face is properly aligned.
- **Visualization:** Displays the aligned image for verification.

---

## Prerequisites

Before running the code, ensure the following are installed on your system:

1. **Python 3.7+**
2. **Dlib**: Install using `pip install dlib`.
3. **OpenCV**: Install using `pip install opencv-python`.
4. **Imutils**: Install using `pip install imutils`.
5. **Facial Landmark Model**: Download [shape_predictor_68_face_landmarks.dat](https://drive.google.com/file/d/1zq1hmJU5IC_dfat_EESRl4pCng_YZjlg/view?usp=drive_link) and place it in the project directory.

---

## Usage

1. Place your input image in the project directory (e.g., `Face.JPG`).
2. Ensure the `shape_predictor_68_face_landmarks.dat` file is in the same directory as the script.
3. Run the script:
   ```bash
   python app.py
