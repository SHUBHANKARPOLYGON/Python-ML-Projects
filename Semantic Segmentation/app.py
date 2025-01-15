import cv2
import numpy as np

# Safely load classes and colors
try:
    with open('ENET/enet-classes.txt') as f:
        classes = f.read().splitlines()

    with open('ENET/enet-colors.txt') as f:
        colors = f.read().splitlines()
        # Parse colors as arrays
        colors = [np.array(col.split(',')).astype('int') for col in colors]
        colors = np.array(colors, dtype='uint8')
except FileNotFoundError as e:
    print(f"File not found: {e}")
    exit()

# Load the pre-trained ENet model
try:
    model = cv2.dnn.readNet('ENET/enet-model.net')
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Open webcam feed
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture frame. Exiting...")
        break

    # Resize input to the expected size (1024x512)
    blob = cv2.dnn.blobFromImage(img, 1/255.0, (1024, 512), (0, 0, 0), swapRB=True, crop=False)
    model.setInput(blob)
    output = model.forward()

    # Extract dimensions from the model's output
    (numClasses, height, width) = output.shape[1:4]

    # Compute the class map and color mask
    classMap = np.argmax(output[0], axis=0)  # (height, width)
    mask = np.zeros((height, width, 3), dtype="uint8")

    # Apply colors based on the class map
    for classID, color in enumerate(colors):
        mask[classMap == classID] = color

    # Resize the mask to match the original input size
    mask = cv2.resize(mask, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)

    # Blend the original image and the segmentation mask
    output = cv2.addWeighted(img, 0.3, mask, 0.7, 0)

    # Display the result
    cv2.imshow('Output', output)
    cv2.imshow('Input', img)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
