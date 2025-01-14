# 🚗 Computer Vision Final Project 🚦

### Subject:
📘 **Computer Vision**

---

### 👥 Members of the Group:
- 🧑‍💻 Matteo Ferrari Marín
- 🧑‍💻 Jorge Moratalla Vita

---

### 📜 Description:
This is our **Computer Vision Final Project**. The project is a fun and interactive application that combines object detection, password authentication, and live video processing. 

Here's how it works:
1. **🔒 Password Authentication**: 
   - The program starts by requiring the user to identify specific geometric shapes (e.g., Triangle, Square, Pentagon) in the correct order to unlock the next stage.
2. **🚗 Car Line Crossing Detection**: 
   - Once unlocked, the program tracks toy cars as they cross a designated finish line.
   - It uses color-based detection to identify and count cars by their color (e.g., green, blue).
3. **🎥 Live Video Processing**: 
   - The system processes frames in real time while displaying the detections on a single window, ensuring seamless visual feedback.

---

### ⚙️ Features:
- 🔍 **Real-time Shape Detection**: Identify and classify geometric shapes using corner detection.
- 🏁 **Finish Line Detection**: Tracks when cars cross a black finish line.
- 🌈 **Color Detection**: Differentiates cars based on predefined color ranges (e.g., HSV for green and blue).
- 🎥 **Video Recording**: Records the entire session in a video file for review.
- 📊 **FPS Counter**: Displays real-time frame rates for performance monitoring.

---

### 📷​ Camera calibration:
- **The results of the camera calibration**:
   Intrinsics:
   [[1.45217681e+03 0.00000000e+00 6.36171498e+02]
   [0.00000000e+00 1.44754507e+03 3.51422378e+02]
   [0.00000000e+00 0.00000000e+00 1.00000000e+00]]

   Distortion coefficients:
   [[-2.55923570e-02 1.37611973e+00 -1.85362544e-03 -3.11270538e-03
   -6.35759530e+00]]

   Root mean squared reprojection error:
   0.8421997191144631

---

### 🛠 How We Did It:
1. **Password Implementation**:  
   - Used **Shi-Tomasi Corner Detection** and a shape classifier to identify geometric patterns. The user must display these patterns in the correct order to proceed.
   
2. **Car Detection and Tracking**:  
   - Developed a color detection system using **HSV color space** to identify cars.
   - Implemented line crossing logic to count cars and track lap times.

3. **Video Processing**:  
   - Utilized the Raspberry Pi camera to capture live video.

4. **Code Modularity**:  
   - Divided the functionality into separate modules for clarity:
     - `password.py`: Handles password verification.
     - `carDetection.py`: Contains logic for car detection and tracking.
     - `main.py`: The main entry point that integrates all components.
     

---

### 🛠️ Project Files:
- `main.py`: The primary script to run the project.
- `password.py`: Handles shape-based password verification.
- `carDetection.py`: Implements color-based car tracking.
- `output_video.avi`: Video file of a recorded session (auto-generated when you run the program).
- `calibrar.py`: Code to find the internal and external parameters of the camera.

---

### 📹 Demo Video:
Click below to see the program in action directly on GitHub!  
![Watch the video](output_video_2.gif)

---

### 🎯 What We've Learned:
- How to apply **corner detection** for shape recognition.
- Techniques for **color-based object tracking** using HSV color space.
- Real-time video processing and optimization in **OpenCV**.
- Modular coding practices to keep projects organized and maintainable.

---
