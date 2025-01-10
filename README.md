# 🚗 Computer Vision Final Project 🚦

### Subject:
📘 **Computer Vision**

---

### 👥 Members of the Group:
- 🧑‍💻 Matteo Ferrari Marín
- 🧑‍💻 Jorge Moratalla Vita

---
### 📜 Codes to check:
- main.py
- calibrar.py
- password.py
- carDetection.py

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
- 🛠 **Single Window Display**: Ensures all interactions occur in the same window for simplicity and user convenience.

---

### 🛠 How We Did It:
1. **Password Implementation**:  
   - Used **Shi-Tomasi Corner Detection** and a shape classifier to identify geometric patterns. The user must display these patterns in the correct order to proceed.
   
2. **Car Detection and Tracking**:  
   - Developed a color detection system using **HSV color space** to identify cars.
   - Implemented line crossing logic to count cars and track lap times.

3. **Video Processing**:  
   - Utilized the Raspberry Pi camera to capture live footage.
   - Integrated **OpenCV** for real-time processing and rendering.

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

### 🚀 Getting Started:
1. Clone this repository:
   ```bash
   git clone https://github.com/your_repo.git
   cd your_repo
