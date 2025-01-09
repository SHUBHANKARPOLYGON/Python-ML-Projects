import cv2
import dlib
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(0)  # 0 for default webcam, change to 1 or other index for external cameras

# Load the age detection model
age_prototxt = "Model/age_deploy.prototxt"
age_caffemodel = "Model/age_net.caffemodel"

try:
    age_Net = cv2.dnn.readNetFromCaffe(age_prototxt, age_caffemodel)
except Exception as e:
    print(f"Error loading age detection model: {e}")
    exit()

# Define age categories and preprocessing requirements
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)',
           '(25-32)', '(38-43)', '(48-53)', '(60-100)']
model_mean = (78.4263377603, 87.7689143744, 114.895847746)

# Load the face detector
face_detector = dlib.get_frontal_face_detector()

print("Press 'q' to exit the application.")

while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Resize the frame to a manageable size
    frame = cv2.resize(frame, (720, 640))

    # Convert frame to grayscale for face detection
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_detector(img_gray)

    for face in faces:
        x = face.left()
        y = face.top()
        x2 = face.right()
        y2 = face.bottom()

        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x2, y2), (0, 200, 200), 2)

        # Extract the face region
        face_roi = frame[max(0, y):min(y2, frame.shape[0]), max(0, x):min(x2, frame.shape[1])]

        # Preprocess the face region for age prediction
        blob = cv2.dnn.blobFromImage(face_roi, 1.0, (227, 227), model_mean, swapRB=False)

        # Predict the age
        age_Net.setInput(blob)
        age_preds = age_Net.forward()
        age = ageList[np.argmax(age_preds[0])]

        # Display the predicted age on the frame
        cv2.putText(frame, f'Age: {age}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 255, 255), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow("Real-Time Age Detection", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
