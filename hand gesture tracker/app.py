import cv2
import mediapipe as mp
import time

# Initialize Mediapipe hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Configure the hand detection model
hands = mp_hands.Hands(
    static_image_mode=False,       # Use for live video
    max_num_hands=2,              # Detect up to 2 hands
    min_detection_confidence=0.5, # Minimum detection confidence
    min_tracking_confidence=0.5   # Minimum tracking confidence
)

# Open webcam
cap = cv2.VideoCapture(0)

print("Press 'q' to exit.")

# Initialize FPS calculation variables
prev_time = 0


def count_fingers(hand_landmarks):
    """
    Count the number of extended fingers based on landmark positions.
    Returns the number of extended fingers and detects a thumbs-up gesture.
    """
    finger_tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    extended_fingers = 0
    is_thumb_up = False

    # Check the thumb separately (special case for left/right hands)
    if hand_landmarks.landmark[finger_tips[0]].y < hand_landmarks.landmark[finger_tips[0] - 2].y:
        is_thumb_up = True

    # Check other fingers
    for tip in finger_tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            extended_fingers += 1

    return extended_fingers, is_thumb_up

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the image horizontally for a mirror effect and convert to RGB
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and detect hands
    results = hands.process(image_rgb)

    # Draw hand landmarks and count fingers if detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw the hand landmarks and connections
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

            # Count fingers and check for thumbs up
            num_fingers, thumb_up = count_fingers(hand_landmarks)

            # Display the count or gesture on the image
            text = f"Fingers: {num_fingers}"
            if thumb_up and num_fingers == 0:
                text = "Thumbs Up!"

            # Position text on the screen
            cv2.putText(
                image, text, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
            )

    # Calculate and display FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv2.putText(
        image, f"FPS: {int(fps)}", (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2
    )

    # Display the processed video feed
    cv2.imshow('Hand Gesture Tracker', image)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
