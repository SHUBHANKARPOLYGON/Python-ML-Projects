import cv2
import numpy as np

# Load action classes from a file
with open('Models/action_recognition_kinetics.txt') as f:
    classes = f.read().splitlines()

# Open video capture
cap = cv2.VideoCapture(0)

# Check if the video capture is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Duration in terms of frames
duration = 15

# Load the pre-trained model
model = cv2.dnn.readNet('Models/resnet-34_kinetics.onnx')

while True:
    images = []
    for i in range(duration):
        success, img = cap.read()
        if not success:
            print("Error: Failed to capture image from webcam.")
            break
        # Resize the image to match the model's input size and add to list
        resized_img = cv2.resize(img, (500, 500))
        images.append(resized_img)

    if len(images) < duration:
        # Skip processing if we didn't capture enough frames
        continue

    # Convert the list of images to a blob
    blob = cv2.dnn.blobFromImages(
        images, 
        scalefactor=1.0, 
        size=(112, 112), 
        mean=(114.7748, 107.7354, 99.4750), 
        swapRB=True, 
        crop=True
    )

    # Reshape blob for the model's expected input
    blob = np.transpose(blob, (1, 0, 2, 3))
    blob = np.expand_dims(blob, axis=0)

    # Set the blob as input to the model
    model.setInput(blob)
    outputs = model.forward()

    # Get the predicted class label
    label = classes[np.argmax(outputs)]

    # Display the label on each frame
    for img in images:
        cv2.putText(img, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.imshow('Action Recognition', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()
