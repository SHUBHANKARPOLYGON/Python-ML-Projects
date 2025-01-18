# Video to Frame Extraction
This project demonstrates how to extract frames from a video file and save them as image files. It is implemented using Python with the OpenCV library. Specifically, it saves every alternate frame from the input video to an output directory.

### Features
- Reads an input video file.
- Saves every alternate frame (even-numbered frames) as image files.
- Automatically creates an output directory named after the input video file for storing the frames.
- Simple and efficient frame extraction using OpenCV.

### Prerequisites

Make sure you have the following installed on your system:

- Python (3.6 or later recommended)
- OpenCV library (```cv2```)
- A valid video file for testing (```.mp4```, ```.avi```, etc.)
To install OpenCV, run:

```bash
pip install opencv-python
```
### How to Use

1. Place your video file in the same directory as the script, or update the video_path variable with the path to your video file.
2. Run the script:
```bash
python app.py
```
3. The program will create a directory named after your video file (e.g., ```sample_video Output Frames/```) and save the frames inside this directory.

### Key Variables
- ```video_path```: Path to the input video file.
- ```save_dir```: Directory where frames will be saved.
- ```count```: Frame counter to track and save alternate frames.

### Output

For an input video file named ```sample_video.mp4```, the output will be:

A directory named ```sample_video Output Frames/```
Saved frames as ```frame0000.jpg```, ```frame0002.jpg```, ```frame0004.jpg```, etc.

### Sample Output
```bash
Saved: sample_video Output Frames/frame0000.jpg  
Saved: sample_video Output Frames/frame0002.jpg  
Saved: sample_video Output Frames/frame0004.jpg  
...  
Frames successfully saved to sample_video Output Frames/
```

## Customization

- To save all frames (instead of alternate frames), remove the condition:
```bash
if count % 2 == 0:
```

- To save frames in a different format (e.g., PNG), modify the file extension in:
```bash
frame_filename = os.path.join(save_dir, f"frame{count:04d}.png")
```