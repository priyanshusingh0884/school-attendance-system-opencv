import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os

# Initialize webcam
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not access webcam.")
    exit()


# Load known faces
known_face_encoding = []
known_face_names = []

students = []

# Student image details
student_images = {
    "Priyanshu": "faces/priyanshu.jpg",
    "Lucky": "faces/lucky.jpg"
}

# Extract facial encodings
for name, image_path in student_images.items():

    if not os.path.exists(image_path):
        print(f"Warning: Image not found for {name}: {image_path}")
        continue

    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)

    if len(encodings) == 0:
        print(f"Warning: No face detected in {image_path}")
        continue

    known_face_encoding.append(encodings[0])
    known_face_names.append(name)

students = known_face_names.copy()

if not known_face_names:
    print("Error: No valid student faces loaded.")
    video_capture.release()
    exit()


# Create attendance CSV file
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

attendance_file = open(
    f"{current_date}.csv",
    "w",
    newline=""
)

lnwriter = csv.writer(attendance_file)

# Write CSV header
lnwriter.writerow(["Name", "Time"])


try:

    while True:

        ret, frame = video_capture.read()

        if not ret:
            print("Failed to capture video frame.")
            break

        # Resize frame for faster face recognition
        small_frame = cv2.resize(
            frame,
            (0, 0),
            fx=0.25,
            fy=0.25
        )

        # Detect faces
        face_locations = face_recognition.face_locations(small_frame)

        face_encodings = face_recognition.face_encodings(
            small_frame,
            face_locations
        )

        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(
                known_face_encoding,
                face_encoding
            )

            face_distance = face_recognition.face_distance(
                known_face_encoding,
                face_encoding
            )

            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:

                name = known_face_names[best_match_index]

                # Mark attendance only once
                if name in students:

                    students.remove(name)

                    current_time = datetime.now().strftime("%H:%M:%S")

                    lnwriter.writerow([name, current_time])
                    attendance_file.flush()

                    print(f"Attendance marked: {name} at {current_time}")

            else:
                name = "Unknown"

            # Display name on webcam
            cv2.putText(
                frame,
                name,
                (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                2
            )

        # Display webcam window
        cv2.imshow("School Attendance System", frame)

        # Press q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


finally:

    # Release webcam and close files
    video_capture.release()
    cv2.destroyAllWindows()
    attendance_file.close()

    print("Attendance system closed.")
