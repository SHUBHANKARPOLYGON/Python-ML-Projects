import cv2
import os

# Read the image
image_path = 'Face.jpg'  # Replace with the correct path to your image
haarcascade_path = 'haarcascade_frontalface_default.xml'  # Path to Haar cascade

# Check if the image and Haar cascade file exist
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image file '{image_path}' not found.")
if not os.path.exists(haarcascade_path):
    raise FileNotFoundError(f"Haar cascade file '{haarcascade_path}' not found.")

# Load the image
img = cv2.imread(image_path)
if img is None:
    raise ValueError(f"Unable to read the image '{image_path}'.")

# Load the Haar cascade
faceCascade = cv2.CascadeClassifier(haarcascade_path)
if faceCascade.empty():
    raise ValueError("Failed to load Haar cascade file.")

# Detect faces
faces = faceCascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4)

# Prepare the output directory
output_dir = os.path.join(os.getcwd(), 'Extract_Faces_From_Image', 'Faces')
os.makedirs(output_dir, exist_ok=True)

# Save each detected face as a separate image
if len(faces) == 0:
    print("No faces detected.")
else:
    print(f"Detected {len(faces)} face(s). Saving to {output_dir}...")
    for i, (x, y, w, h) in enumerate(faces, start=1):
        FaceImg = img[y:y+h, x:x+w]
        filename = os.path.join(output_dir, f'Face{i}.jpg')
        cv2.imwrite(filename, FaceImg)
    print("Faces saved successfully.")
