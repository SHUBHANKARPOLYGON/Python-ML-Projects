import cv2
import dlib
import math
from imutils import rotate_bound

# File paths
image_path = 'Face.jpg'
predictor_path = 'shape_predictor_68_face_landmarks.dat'

# Load the image
img = cv2.imread(image_path)
if img is None:
    raise ValueError(f"Image not found at path: {image_path}")

# Initialize Dlib's face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

# Points to calculate angle
face_points = [27, 30]  # Landmarks for nose bridge and tip

def get_angle(points):
    """
    Calculate the angle between three points.
    """
    b, c, a = points[-3:]  # Reference points: nose bridge, adjusted point, and tip
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    ang = (ang + 360) % 360  # Normalize angle to [0, 360]
    print(f"Calculated angle: {ang}")
    return ang

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = detector(img_gray)
if not faces:
    raise ValueError("No faces detected in the image.")

# Process each detected face
points = []  # To store the selected landmarks
for face in faces:
    # Get facial landmarks
    landmarks = predictor(img_gray, face)
    for i in face_points:
        x = landmarks.part(i).x
        y = landmarks.part(i).y
        points.append([x, y])
        if i == 27:  # Adjust point below the nose bridge
            points.append([x, y + 20])
        print(f"Landmark {i}: ({x}, {y})")

# Ensure enough points for angle calculation
if len(points) < 3:
    raise ValueError("Insufficient points for angle calculation.")

# Calculate angle and rotate the image
angle = get_angle(points)
img_aligned = rotate_bound(img, angle)

# Display aligned image
cv2.imshow('Aligned Image', img_aligned)
cv2.waitKey(0)
cv2.destroyAllWindows()
