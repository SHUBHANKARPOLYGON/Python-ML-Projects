# Cartoonized Capture 

## Overview
This Python script captures video from your webcam and applies a cartoonization effect in real-time. The cartoonized frames are displayed in a window, and you can save the processed images by pressing the spacebar. Exit the application by pressing the `q` key.

## Features
- Real-time video feed with cartoonized effect.
- Save cartoonized images by pressing the spacebar.
- Easy-to-use interface with `OpenCV`.
- Automatically creates a directory to store saved images.

## Requirements
To run this script, you need the following:

- Python 3.x
- OpenCV library (`cv2`)

Install OpenCV using pip if not already installed:
```bash
pip install opencv-python
```

## Usage
1. Ensure you have a webcam connected to your system.
2. Save the script as `cartoonize_capture.py`.
3. Run the script:
   ```bash
   python cartoonize_capture.py
   ```
4. Instructions while running:
   - Press `q` to quit the application.
   - Press the spacebar to save the current cartoonized frame.

## Saved Images
- Saved images are stored in a folder named `Cartoonized_Images` in the same directory as the script.
- Images are saved with the naming format `Image_<number>.jpg`.

## Code Explanation
### Cartoonization Process
1. **Grayscale Conversion**:
   - The input frame is converted to grayscale to detect edges.

2. **Edge Detection**:
   - Adaptive thresholding is used to create a binary edge mask.

3. **Smoothing**:
   - Bilateral filtering smooths the image while preserving edges.

4. **Combining**:
   - The edge mask is combined with the smoothed image to produce a cartoonized effect.

### Key Functions
- **cartoonize_image(img)**:
  - Converts the input image to a cartoonized version.

- **cv2.VideoCapture(0)**:
  - Captures live video feed from the webcam.

- **cv2.imshow()**:
  - Displays the processed video feed in a window.

- **cv2.imwrite()**:
  - Saves the current frame as a JPEG image.
---

## Troubleshooting
- **Error: Unable to access the camera**:
  - Ensure your webcam is connected and not used by another application.

- **Saved images are not appearing**:
  - Check if the `Cartoonized_Images` folder is created in the same directory as the script.

## License
This script is open-source and free to use. Modify and distribute as needed.

## Author
Developed by [Shubhankar Tiwary] with ❤️.
