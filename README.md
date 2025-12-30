# Palm Detection Web Application

A Flask-based web application that utilizes computer vision to detect and track palm gestures in real-time using a webcam. This project demonstrates hand landmark detection and confidence-based scanning for potential biometric or interactive applications.

---

## 🚀 Features

- Real-time palm detection using MediaPipe Hands
- Live video streaming from webcam
- Confidence-based scanning mechanism
- Responsive web interface with multiple pages
- Dynamic template rendering with Flask

---

## 🧩 Project Structure

```
final-year-project--main/
│
├── app.py                 # Main Flask application
├── camera.py              # Camera and hand detection logic
├── static/
│   └── images/            # Static image assets
├── templates/
│   ├── index.html         # Home page
│   ├── scan.html          # Scanning interface
│   └── about.html         # About page
├── README.md              # Project documentation
└── __pycache__/           # Python cache files
```

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.7+
- Webcam (built-in or external)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/final-year-project--main.git
cd final-year-project--main
```

### 2️⃣ Create and Activate Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install flask opencv-python mediapipe
```

### 4️⃣ Run the Application

```bash
python app.py
```

The application will start at: `http://127.0.0.1:5000/`

---

## 🧠 How It Works

### **Routes**

- `/` → Home page (index.html)
- `/scan` → Scanning interface (scan.html)
- `/start-scan` → API endpoint to initiate scanning
- `/check-palm` → API endpoint to check palm detection status
- `/video` → Live video stream endpoint
- `/about` → About page (about.html)

### **Palm Detection Process**

1. User navigates to the scan page
2. Clicks "Start Scan" to begin detection
3. Application captures webcam feed and processes frames using MediaPipe
4. Detects hand landmarks and tracks palm presence
5. Builds confidence score until reaching 100%
6. Automatically stops scanning when confidence threshold is met

### **Technical Details**

- Uses OpenCV for camera capture and image processing
- MediaPipe Hands for accurate hand landmark detection
- Flask for web framework and API endpoints
- Real-time video streaming with multipart responses

---

## 🛠️ Technologies Used

- **Flask**: Web framework for Python
- **OpenCV**: Computer vision library
- **MediaPipe**: AI-powered hand tracking
- **HTML/CSS/JavaScript**: Frontend interface
- **Jinja2**: Template engine

---

## 📋 Usage

1. Open your browser and go to `http://127.0.0.1:5000/`
2. Navigate to the Scan page
3. Allow camera access when prompted
4. Click "Start Scan" and position your palm in front of the camera
5. Wait for the confidence meter to reach 100%
6. Scan completes automatically

---

## 🧾 Troubleshooting

### Camera Not Working

- Ensure your webcam is not being used by another application
- Check camera permissions in your browser
- Try refreshing the page and granting camera access

### Import Errors

- Make sure all dependencies are installed: `pip install flask opencv-python mediapipe`
- If using a virtual environment, ensure it's activated

### Template Not Found Error

- Verify that HTML files are in the `templates/` directory
- Ensure the directory structure matches the project structure above

---

## 👨‍💻 Author

**CodeXpert**  
📦 GitHub: [hustler.kunal\_](https://github.com/hustler-kunal)

---

## 📄 License

This project is for educational purposes as part of a final year project. Please refer to the license file if available.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📞 Contact

For questions or feedback, please reach out via GitHub issues.

## 📜 License

This project is open-source and free to use.
