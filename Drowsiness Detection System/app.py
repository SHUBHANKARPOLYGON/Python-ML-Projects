import cv2
import dlib
import pyttsx3
from scipy.spatial import distance

# Initialize pyttsx3 for audio alerts
engine = pyttsx3.init()

# Initialize the webcam (use 0 for default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not found or unable to access!")
    exit()

# Load the face detector
face_detector = dlib.get_frontal_face_detector()

# Load the shape predictor for facial landmarks
try:
    dlib_facelandmark = dlib.shape_predictor("Model/shape_predictor_68_face_landmarks.dat")
except Exception as e:
    print(f"Error: {e}")
    print("Make sure the .dat file is available in the specified path.")
    exit()

# Function to calculate the Eye Aspect Ratio (EAR)
def detect_eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    aspect_ratio = (A + B) / (2.0 * C)
    return aspect_ratio

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame from camera.")
        break

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_detector(gray_frame)

    for face in faces:
        # Get the landmarks for the face
        face_landmarks = dlib_facelandmark(gray_frame, face)
        left_eye = []
        right_eye = []

        # Extract points for the right eye (indices 42 to 47 in the .dat file)
        for n in range(42, 48):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            right_eye.append((x, y))
            next_point = n + 1 if n != 47 else 42
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

        # Extract points for the left eye (indices 36 to 41 in the .dat file)
        for n in range(36, 42):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            left_eye.append((x, y))
            next_point = n + 1 if n != 41 else 36
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (255, 255, 0), 1)

        # Calculate EAR for both eyes
        right_eye_ratio = detect_eye_aspect_ratio(right_eye)
        left_eye_ratio = detect_eye_aspect_ratio(left_eye)
        avg_eye_ratio = (left_eye_ratio + right_eye_ratio) / 2.0

        # Round EAR value for better readability
        avg_eye_ratio = round(avg_eye_ratio, 2)

        # Check for drowsiness based on EAR threshold
        if avg_eye_ratio < 0.25:
            cv2.putText(frame, "DROWSINESS DETECTED", (50, 100),
                        cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)
            cv2.putText(frame, "Alert! Wake up!", (50, 450),
                        cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 212), 3)
            
            # Audio alert
            engine.say("Alert! Wake up!")
            engine.runAndWait()

    # Display the frame with annotations
    cv2.imshow("Drowsiness Detector", frame)

    # Exit if 'q' key is pressed
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
