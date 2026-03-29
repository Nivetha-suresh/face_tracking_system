import streamlit as st
import cv2
from face_detector import detect_faces
from gender_detector import detect_gender

st.title("Real-Time Face Tracking and Gender Detection System")

run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()

    if not ret:
        st.error("Camera not working")
        break

    faces = detect_faces(frame)

    people_count = len(faces)

    for face in faces:
        x1, y1, x2, y2 = face

        gender = detect_gender(frame, face)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.putText(frame, gender, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 255, 255), 2)

    cv2.putText(frame, f'People Count: {people_count}', (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    FRAME_WINDOW.image(frame)

camera.release()