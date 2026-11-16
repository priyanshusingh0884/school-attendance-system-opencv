# 🎓 School Attendance System using OpenCV

An automated school attendance system developed using Python, OpenCV and the face_recognition library. The application identifies registered students through a webcam and records their attendance with timestamps in a CSV file.

## ✨ Features

- Real-time face detection.
- Face recognition using facial encodings.
- Webcam integration.
- Automatic attendance marking.
- Prevents duplicate attendance entries during a session.
- Records attendance with timestamps.
- Stores attendance records in CSV format.

## 🛠️ Technologies Used

- Python
- OpenCV
- face_recognition
- NumPy
- CSV
- Datetime

## 📦 Installation

Install the required dependencies:

```bash
pip install opencv-python face-recognition numpy
```

The face_recognition library may require additional system dependencies, including CMake and dlib.

## 📁 Project Setup

1. Clone this repository.
2. Create a folder named `faces`.
3. Add authorised student images to the folder.
4. Update the image paths and student names in the Python script.
5. Connect a webcam.

## ▶️ How to Run

Execute:

```bash
python main.py
```

The application will open the webcam and start recognising registered students.

Press `q` to exit.

## 📊 Attendance Records

Attendance is stored in a CSV file named according to the current date.

Each record contains:

- Student name
- Attendance time

## 📚 What I Learned

- Computer vision fundamentals.
- Real-time webcam processing.
- Face detection and recognition.
- Facial encoding comparison.
- Image processing using OpenCV.
- CSV file handling.
- Automating attendance recording.

## ⚠️ Privacy Notice

This project processes facial images for educational purposes. Use it only with the informed consent of participants. Store biometric images and attendance records securely.
