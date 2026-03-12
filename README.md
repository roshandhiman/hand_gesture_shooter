# AI Hand Gesture Shooter 🎯

A real-time computer vision shooting game controlled using hand gestures.  
The game uses MediaPipe hand tracking, OpenCV camera processing, and Pygame rendering to allow players to aim and shoot moving targets using only their index finger movements.

This project demonstrates the integration of computer vision, gesture recognition, and game development in Python.

--------------------------------------------------

FEATURES

- Real-time hand tracking using MediaPipe
- Finger-controlled crosshair system
- Gesture-based shooting detection
- Smooth crosshair movement
- Moving colorful targets
- Hit detection and scoring system
- Real-time gameplay

--------------------------------------------------

TECHNOLOGIES USED

Python — Core programming language  
OpenCV — Webcam capture and frame processing  
MediaPipe — Real-time hand landmark detection  
Pygame — Game rendering and UI  
NumPy — Mathematical calculations

--------------------------------------------------

HOW THE GAME WORKS

1. The webcam captures live video frames.
2. MediaPipe detects the user's hand and tracks 21 hand landmarks.
3. The index finger tip controls the crosshair position.
4. A quick upward finger motion triggers a shoot gesture.
5. If the crosshair overlaps a target, the target is destroyed and the score increases.

Game Flow:

Camera → Hand Detection → Finger Coordinates → Crosshair Movement → Shoot Detection → Hit Detection → Score Update

--------------------------------------------------

INSTALLATION

Clone the repository

git clone https://github.com/YOUR_USERNAME/hand_gesture_shooter.git
cd hand_gesture_shooter

Install dependencies

pip install opencv-python mediapipe pygame numpy

Run the game

python main.py

--------------------------------------------------

CONTROLS

Move Index Finger → Aim

Quick Finger Flick Up → Shoot

Crosshair Color:

White → No target  
Red → Target locked

--------------------------------------------------

PROJECT STRUCTURE

hand_gesture_shooter
│
├── main.py
├── README.md
└── requirements.txt

--------------------------------------------------

FUTURE IMPROVEMENTS

- Gun recoil animation
- Particle explosion effects
- Sound effects
- Enemy AI system
- Multiplayer mode
- Gesture-based reload system

--------------------------------------------------

AUTHOR

Roshanpreet Singh

GitHub  
https://github.com/roshandhiman

--------------------------------------------------

If you like this project, please consider giving it a star on GitHub.
