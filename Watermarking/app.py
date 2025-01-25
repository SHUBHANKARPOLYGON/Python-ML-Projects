import cv2
import numpy as np

# Paths to the watermark and image
path_watermark = 'watermark_path.png'
path_img = 'image_path.jpg'

# Load the watermark and the main image
logo = cv2.imread(path_watermark, cv2.IMREAD_UNCHANGED)  # Load with alpha channel if present
img = cv2.imread(path_img)

# Ensure both images are loaded successfully
if logo is None or img is None:
    print("Error: One or more images could not be loaded.")
    exit()

# Get dimensions of the watermark and the main image
h_logo, w_logo, _ = logo.shape
h_img, w_img, _ = img.shape

# Resize watermark if larger than the main image
if h_img <= h_logo or w_img <= w_logo:
    scale_factor = min(h_img / (3 * h_logo), w_img / (3 * w_logo))
    logo = cv2.resize(logo, (int(w_logo * scale_factor), int(h_logo * scale_factor)), interpolation=cv2.INTER_AREA)
    h_logo, w_logo, _ = logo.shape

# Define the position for placing the watermark
gap_x, gap_y = 25, 20
top_y = h_img - gap_y - h_logo
left_x = gap_x
bottom_y = h_img - gap_y
right_x = gap_x + w_logo

# Ensure the watermark has an alpha channel for transparency
if logo.shape[2] < 4:  # Add alpha channel if missing
    alpha_channel = np.ones((h_logo, w_logo), dtype=np.uint8) * 255
    logo = np.dstack([logo, alpha_channel])

# Extract the alpha channel from the watermark
alpha = (logo[:, :, 3] / 255.0) * 0.5  # Adjust opacity to 50% (lower values for less visibility)
overlay = logo[:, :, :3]  # The color part of the watermark

# Extract the ROI from the main image
roi = img[top_y:bottom_y, left_x:right_x]

# Blend the watermark with the ROI
for c in range(0, 3):  # Blend each color channel
    roi[:, :, c] = (alpha * overlay[:, :, c] + (1 - alpha) * roi[:, :, c])

# Replace the ROI in the main image
img[top_y:bottom_y, left_x:right_x] = roi

# Show and save the final image
cv2.imshow('Image with Subtle Watermark', img)
cv2.imwrite('watermarked_' + path_img.split('/')[-1], img)
cv2.waitKey(0)
cv2.destroyAllWindows()
