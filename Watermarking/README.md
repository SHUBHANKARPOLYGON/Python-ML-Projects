# Watermark Application 

This project provides a Python script for overlaying a subtle, semi-transparent watermark on an image using OpenCV. The script is designed to handle watermark resizing and placement while ensuring compatibility with a wide range of image dimensions.

---

## Features
1. **Watermark Resizing**:
   - Automatically resizes the watermark to fit the dimensions of the main image if it's too large.
2. **Custom Placement**:
   - Positions the watermark near the bottom-left corner with configurable margins.
3. **Transparency Control**:
   - Applies a 50% transparency effect to the watermark for a subtle overlay.
4. **Error Handling**:
   - Ensures proper image loading and exits gracefully if there are issues.
5. **Output**:
   - Displays the final watermarked image and saves it to the local directory.

---

## Prerequisites
Ensure the following Python libraries are installed:
- `opencv-python` (`cv2`)
- `numpy`

To install these dependencies, run:
```bash
pip install opencv-python numpy
```

---

## Usage
1. **Prepare Your Assets**:
   - Place the watermark image (e.g., `watermark.png`) and the main image (e.g., `image.jpg`) in the desired directory.
   - Ensure the watermark image supports transparency (e.g., PNG with an alpha channel).

2. **Configure Paths**:
   - Update the script with the correct file paths:
     ```python
     path_watermark = 'path/to/your/watermark.png'
     path_img = 'path/to/your/image.jpg'
     ```

3. **Run the Script**:
   Execute the script:
   ```bash
   python app.py
   ```

4. **Output**:
   - The script displays the watermarked image in a new window.
   - The resulting file is saved with the prefix `watermarked_` in the same directory as the main image.

---

## Key Code Details
### Watermark Resizing
The watermark is resized if it exceeds one-third of the main image’s dimensions:
```python
if h_img <= h_logo or w_img <= w_logo:
    scale_factor = min(h_img / (3 * h_logo), w_img / (3 * w_logo))
    logo = cv2.resize(logo, (int(w_logo * scale_factor), int(h_logo * scale_factor)), interpolation=cv2.INTER_AREA)
```

### Transparency Application
Transparency is applied using the alpha channel, adjusted to 50% visibility:
```python
alpha = (logo[:, :, 3] / 255.0) * 0.5
```

### ROI Blending
The watermark is blended into the image using a weighted average:
```python
for c in range(0, 3):
    roi[:, :, c] = (alpha * overlay[:, :, c] + (1 - alpha) * roi[:, :, c])
```

---

## Notes
- Adjust `gap_x` and `gap_y` to change the watermark's placement.
- If your watermark lacks an alpha channel, the script adds one automatically.

---

## Example
**Input Images**:
- Main Image: `image.jpg`
- Watermark: `watermark.png`

**Result**:
- Output Image: `watermarked_image.jpg` (with a subtle watermark in the bottom-left corner).

---

