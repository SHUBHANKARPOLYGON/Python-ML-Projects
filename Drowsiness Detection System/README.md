# Drowsiness Detection System

This project implements a real-time drowsiness detection system using a webcam. It monitors a person's eye aspect ratio (EAR) to detect signs of drowsiness and provides visual and audio alerts if the EAR drops below a threshold.

---

## Features

1. **Real-Time Eye Tracking**: Detects and tracks eye landmarks using a pre-trained dlib model.
2. **Eye Aspect Ratio (EAR) Calculation**: Computes the EAR to measure eye closure levels.
3. **Drowsiness Alerts**:
   - **Visual Alert**: Displays "DROWSINESS DETECTED" on the screen.
   - **Audio Alert**: Speaks an alert message using the `pyttsx3` library.
4. **Customizable Thresholds**: Allows adjustment of the EAR threshold to fine-tune sensitivity.

---

## Requirements

### Libraries
This project requires the following Python libraries:
- `opencv-python`: For video capture and frame processing.
- `dlib`: For face and facial landmark detection.
- `pyttsx3`: For audio alerts.
- `scipy`: For calculating Euclidean distances in EAR computation.

Install the required libraries using pip:
```bash
pip install opencv-python dlib pyttsx3 scipy
```

Run the Script

```
python app.py
```

## Download the Model:

- Link:- [Drowsiness Detection System Model](https://drive.google.com/file/d/1zq1hmJU5IC_dfat_EESRl4pCng_YZjlg/view?usp=sharing)
