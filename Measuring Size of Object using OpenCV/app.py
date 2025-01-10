import cv2
import numpy as np

# Load the image
img = cv2.imread('Images/1.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a threshold to the image to separate the objects from the background
ret, thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find the contours of the objects in the image
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Known width or height of a reference object in the real world (e.g., in cm)
reference_width_cm = 5.0  # Replace with the actual width of the reference object in cm

# Bounding box of the reference object (manually determine or detect automatically)
# Update this with your reference object's bounding box values
reference_contour = max(contours, key=cv2.contourArea)  # Assuming the largest contour is the reference
x_ref, y_ref, w_ref, h_ref = cv2.boundingRect(reference_contour)
reference_width_px = w_ref  # Width of the reference object in pixels

# Calculate pixel-to-centimeter ratio
pixel_to_cm_ratio = reference_width_cm / reference_width_px

# Loop through the contours and calculate the size of each object
for cnt in contours:
    # Calculate area in pixels
    area_px = cv2.contourArea(cnt)

    # Draw a bounding box around each object
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Convert area and dimensions to centimeters
    width_cm = w * pixel_to_cm_ratio
    height_cm = h * pixel_to_cm_ratio
    area_cm2 = area_px * (pixel_to_cm_ratio ** 2)

    # Display object dimensions and area on the image
    text = f"{width_cm:.1f}cm x {height_cm:.1f}cm"
    cv2.putText(img, text, (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(img, f"{area_cm2:.1f}cm²", (x, y + h + 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Show the final image with the bounding boxes and sizes of the objects
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
