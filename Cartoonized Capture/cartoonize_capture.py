import cv2

def cartoonize_image(img):
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=9
    )

    # Apply bilateral filter to smooth the image while preserving edges
    color = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    # Combine the edges and the smoothed color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

cap = cv2.VideoCapture(0)
count = 1

if not cap.isOpened():
    print("Error: Unable to access the camera.")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Error: Unable to read frame from the camera.")
        break

    # Apply the cartoonization function
    cartoon_img = cartoonize_image(img)

    # Display the cartoonized image
    cv2.imshow('Cartoonized Capture', cartoon_img)

    # Check for user input
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        # Quit the application
        break
    elif key == 32:  # Spacebar to capture the image
        # Save the cartoonized image
        filename = f'Cartoonized_Images/Image_{count}.jpg'
        count += 1
        # Create the directory if it doesn't exist
        import os
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        cv2.imwrite(filename, cartoon_img)
        print(f"Image saved: {filename}")

# Release the video capture object and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
