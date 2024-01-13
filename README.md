# Hand Gesture Control for DJI Tello Drone

## Overview
This repository provides a demonstration of controlling a DJI Tello drone in the AirSim environment using hand gestures detected via the MediaPipe library. By utilizing computer vision techniques, the code interprets hand movements captured by the webcam to command the drone to perform specific actions.

### Features
- Hand Gesture Recognition: Utilizes MediaPipe's Hand module to detect and analyze hand landmarks in real-time from the webcam feed.
- Drone Control: Interprets recognized hand gestures to control the DJI Tello drone's movements in the AirSim simulator.
- Gesture Mapping: Maps specific finger configurations to predefined drone movements (e.g., up, down, left, right).
- User Interface: Displays a live feed with hand landmarks drawn and a label indicating the recognized gesture.

### Requirements
- Python 3.x
- OpenCV (cv2)
- MediaPipe (mediapipe)
- AirSim Python API (airsim)
- Tello Python library (tellolib)

### Installation
1. Clone this repository.
2. Install required libraries by running: `pip install -r requirements.txt`.

### Usage
1. Connect to AirSim: Ensure AirSim is running and connect to the simulator.
2. Connect DJI Tello Drone: Ensure the Tello drone is connected and accessible.
3. Run the Python script airsim_hand_gesture_control.py.
4. Perform hand gestures in front of your webcam.
5. The recognized gestures will control the Tello drone's movements within the AirSim environment.

## Code Structure
This repository provides four distinct code files catering to different functionalities:

### AirSim Integrated Control with Gesture Recognition
- **File Name:** airsim_hand_gesture_control.py
- **Description:** This script integrates both hand gesture recognition using MediaPipe and control commands for the DJI Tello drone in the AirSim environment.

### MediaPipe Hand Gesture Recognition Only
- **File Name:** mediapipe_hand_gesture.py
- **Description:** This script focuses solely on hand gesture recognition using MediaPipe's Hand module. It serves as a standalone demonstration of hand gesture recognition without drone control functionalities.

### AirSim Controlled DJI Tello Drone with Limitations
- **File Name:** tello_control.py
- **Description:** This script provides a simplified version of the AirSim integration for controlling the DJI Tello drone based on hand gestures. It imposes certain limitations on the drone's movements to ensure safer operation.

### AirSim Controlled DJI Tello Drone with Safety Measures
- **File Name:** airsim_limitations.py
- **Description:** Similar to tello_control.py, this script adds additional safety measures to drone movements, preventing continuous or excessive maneuvers.

Users can choose the script based on their requirements:
- Use airsim_hand_gesture_control.py for integrating hand gesture control with the DJI Tello drone in the AirSim simulator.
- Use mediapipe_hand_gesture.py for a standalone demonstration of hand gesture recognition without drone control functionalities.
- Use tello_control.py for controlling the DJI Tello drone with added limitations on movements for safety.
- Use airsim_limitations.py for a version with extended safety measures in drone control.

## Acknowledgments
- AirSim: Utilized for the drone simulation environment.
- MediaPipe: Used for real-time hand landmark detection.
- OpenCV: Employed for image processing and webcam capture.
- Tello Python library: Used for communication with the DJI Tello drone.

## License
This project is licensed under the MIT License.

## Contribution
Contributions are welcome! Feel free to fork this repository, create pull requests, or open issues for any improvements, bug fixes, or suggestions.
