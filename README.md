# 📌 Real-Time Face Tracking and Gender Detection System

## 🚀 Overview
This project is a real-time computer vision application that detects human faces from a live webcam feed and predicts the gender of each detected individual. It also counts the number of people present in the frame dynamically.

The system leverages deep learning-based pre-trained models for accurate face detection and gender classification, integrated into an interactive web interface using Streamlit.

---

## 🎯 Features
- 🎥 Real-time webcam-based face detection  
- 👥 Automatic people counting  
- 🧠 Gender prediction using deep learning models  
- ⚡ Fast and efficient processing  
- 🌐 Interactive UI using Streamlit  

---

## 🛠️ Tech Stack

### 👨‍💻 Programming Language
- Python

### 📚 Libraries & Frameworks
- OpenCV (cv2) – Image processing and DNN inference  
- Streamlit – Web-based UI  
- NumPy – Array operations  

### 🤖 Deep Learning Models
- Face Detection Model (OpenCV DNN)
- Gender Classification Model (Caffe)

---

## 📂 Project Working
The webcam captures live video frames.
Each frame is processed using OpenCV's DNN module.
Faces are detected using a pre-trained face detection model.
Detected faces are cropped and passed to a gender classification model.
The system:
Draws bounding boxes around faces
Displays predicted gender
Shows total people count
