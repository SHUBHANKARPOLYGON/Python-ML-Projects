import cv2
import os

# Input video file
video_path = 'sample_video.mp4'

# Generate output directory name based on the input video file
video_name = os.path.splitext(os.path.basename(video_path))[0]
save_dir = f"{video_name} Output Frames/"

# Create output directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Open the video file
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"Error: Unable to open video file {video_path}")
    exit()

count = 0  # Frame counter

while True:
    ret, frame = cap.read()  # Read a frame from the video

    if not ret:  # Break loop if no more frames
        break

    # Save every alternate frame (e.g., even-numbered frames)
    if count % 2 == 0:
        frame_filename = os.path.join(save_dir, f"frame{count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        print(f"Saved: {frame_filename}")

    count += 1

# Release resources
cap.release()
cv2.destroyAllWindows()

print(f"Frames successfully saved to {save_dir}")
