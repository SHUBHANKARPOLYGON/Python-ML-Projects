# ENet Real-Time Semantic Segmentation

This project demonstrates real-time semantic segmentation using the ENet model with OpenCV's DNN module. The application performs segmentation on live webcam input and visualizes the segmented output.

- Download Models:- [ENET Models and txt's](https://drive.google.com/drive/folders/1CRgrTiEq2XEmS_SkW0HIyFRJND-yMIQP?usp=drive_link)

---

## Features

- Real-time segmentation on live video.
- Overlays segmented masks with the original frame for visualization.
- Configurable color mappings and class labels.

---

## Prerequisites

Ensure you have the following dependencies installed:

- Python 3.7+
- OpenCV (4.5+ recommended)
- NumPy

You will also need the following files:

1. **ENet model:** `enet-model.net`
2. **Class labels:** `enet-classes.txt`
3. **Color mappings:** `enet-colors.txt`

---

## Setup

### 1. Install Required Libraries

```bash
pip install opencv-python numpy
```

### 2. Clone the Repository

```bash
git clone https://github.com/SHUBHANKARPOLYGON/Semantic Segmentation
cd Semantic Segmentation
```

### 3. Download Necessary Files

Place the following files in the `ENET/` directory:

- `enet-model.net`
- `enet-classes.txt`
- `enet-colors.txt`

Ensure the directory structure is as follows:

```
ENET/
  enet-model.net
  enet-classes.txt
  enet-colors.txt
script.py
```

---

## Usage

### Run the Script

```bash
python app.py
```

### Controls

- Press **`q`** to exit the application.

---

## Code Explanation

### Input Preprocessing

- The input frame from the webcam is resized to match the ENet model's expected input size of **1024x512**.
- The frame is converted into a blob using OpenCV's `blobFromImage` function.

### Model Inference

- The blob is passed to the ENet model using the `cv2.dnn.readNet` method.
- The model outputs a tensor containing class probabilities for each pixel.

### Mask Generation

- The pixel-wise class predictions are mapped to corresponding colors defined in `enet-colors.txt`.
- The segmentation mask is resized to match the input frame size.

### Visualization

- The original frame and segmentation mask are blended using OpenCV's `cv2.addWeighted` function.
- The final output is displayed in a window.

---



## Troubleshooting

1. **Webcam Not Detected:**
   Ensure your webcam is properly connected and accessible.

2. **File Not Found Errors:**
   Verify that the `enet-classes.txt`, `enet-colors.txt`, and `enet-model.net` files exist in the correct directory.

3. **Performance Issues:**
   - Ensure your system meets the hardware requirements for real-time processing.
   - Reduce the input size or use a more efficient model.

---

## Acknowledgments

- [ENet: A Deep Neural Network Architecture for Real-Time Semantic Segmentation](https://arxiv.org/abs/1606.02147)
- OpenCV DNN module documentation.

Feel free to contribute or raise issues to improve this project!
