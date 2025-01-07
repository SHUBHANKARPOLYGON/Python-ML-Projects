import cv2
import numpy as np
import time

# Initialize the camera
cap = cv2.VideoCapture(0)
time.sleep(3)  # Allow the camera to warm up

# Capture the background in an initial frame
for i in range(30):
    ret, background = cap.read()

background = np.flip(background, axis=1)  # Flip the background frame

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = np.flip(frame, axis=1)  # Flip the frame
    
    # Convert the frame from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the HSV range for the color of the cloak (e.g., red color)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    
    mask = mask1 + mask2
    
    # Open and dilate the mask image
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    
    # Create an inverse mask
    mask_inv = cv2.bitwise_not(mask)
    
    # Segment out the cloak from the frame using bitwise and
    res1 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    # Segment out the background from the frame using bitwise and
    res2 = cv2.bitwise_and(background, background, mask=mask)
    
    # Combine the two results
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    
    # Display the final output
    cv2.imshow('Invisibility Cloak', final_output)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
