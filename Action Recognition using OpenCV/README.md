# Action Recognition with OpenCV and ONNX Model

This project performs real-time action recognition using a ResNet-34 model pre-trained on the Kinetics dataset. The application captures video from your webcam, processes the frames, and predicts the action being performed.

- Download Models:- [Action Recognition using OpenCV Models](https://drive.google.com/drive/folders/1UDqfN8jXl-C0d0plKu7x2GhzEKCQBN5-?usp=drive_link)

## Features
- Real-time video capture and action recognition.
- Uses a ResNet-34 ONNX model for action prediction.
- Displays the recognized action on the video frames.

## Requirements
To run this project, ensure you have the following installed:
- Python 3.7 or later
- OpenCV
- NumPy
- A pre-trained ONNX model and a text file with action classes.

## Installation

1. Clone the repository or download the code:
   ```bash
   git clone https://github.com/SHUBHANKARPOLYGON/Action-Recognition-using-OpenCV.git
   cd Action-Recognition-using-OpenCV

2. Install the required Python libraries:
   ```bash
   pip install opencv-python numpy

3. Place the following files in the ```Models/``` directory

- ```resnet-34_kinetics.onnx``` (pre-trained ONNX model for action recognition)
- ```action_recognition_kinetics.txt``` (list of action classes, one per line)

## Usage
1. Ensure your webcam is connected and accessible.

2. Run the Python script:
```
python app.py
```
3. The application will open a video window displaying the webcam feed with the recognized action labeled.

Press ```q``` to exit the application.

## Code Structure
- ```action_recognition.py```: The main script to capture video, process frames, and predict actions using the model.

- ```Models/```: Directory containing the pre-trained ONNX model and the list of action classes.

## Troubleshooting
- If the webcam doesn't open, ensure it's connected and not being used by another application.
- Check the ```Models/``` directory for the correct files:
- ```resnet-34_kinetics.onnx```
- ```action_recognition_kinetics.txt```
- Verify that the action classes in the text file match the output labels of the ONNX model.
## Future Improvements
- Add support for multiple camera inputs.
- Enhance performance with GPU acceleration using OpenCV's DNN module.
- Display action confidence scores alongside predictions
