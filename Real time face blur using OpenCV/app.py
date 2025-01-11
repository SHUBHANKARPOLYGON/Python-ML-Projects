import cv2

# Load the Haar cascade for face detection
cascade = cv2.CascadeClassifier("xml file/haarcascade_frontalface_default.xml")

# Start video capture (0 for default webcam, 1 for external webcam)
video_capture = cv2.VideoCapture(0)

if not cascade.load(cv2.samples.findFile("xml file/haarcascade_frontalface_default.xml")):
    print("Error loading Haar cascade file.")
    exit()

# Loop to continuously capture video frames
while True:
    # Capture the current frame from the video
    ret, frame = video_capture.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Convert the captured frame to grayscale
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = cascade.detectMultiScale(
        gray_image,
        scaleFactor=1.3,  # Adjusted scaleFactor for better accuracy
        minNeighbors=5,   # Minimum neighbors for filtering detections
        minSize=(30, 30)  # Minimum size of the detected face
    )

    for (x, y, w, h) in faces:
        # Draw a green rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # Apply blur to the detected face region
        face_region = frame[y:y+h, x:x+w]
        blurred_face = cv2.medianBlur(face_region, 35)
        frame[y:y+h, x:x+w] = blurred_face

    # Display the video with blurred faces
    cv2.imshow('Face Blurred', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
