# 🎓 IBM AI-Based Smart Attendance Monitoring System

An AI-powered attendance management system that automates student attendance using **Face Recognition**, built with **Python, Flask, OpenCV, and SQLite**.

---

## 📌 Project Overview

The IBM AI-Based Smart Attendance Monitoring System eliminates the need for manual attendance by recognizing students' faces through a webcam. The system automatically records attendance, manages student information, and generates attendance reports.

This project was developed as a **BCA Final Year Project** to demonstrate the practical implementation of Artificial Intelligence and Computer Vision in educational institutions.

---

## ✨ Features

### 👨‍🎓 Student Management
- Register new students
- Edit student information
- Delete students
- Search students by ID or Name

### 📷 Face Dataset Generation
- Capture 100 face images per student
- Automatic dataset organization
- Recapture dataset when required

### 🤖 Face Recognition
- Real-time face detection
- Automatic attendance marking
- Unknown face detection

### 📊 Attendance Management
- Daily attendance recording
- Attendance reports
- Search attendance records
- Filter by date
- Export reports to CSV

### 📈 Dashboard
- Total Students
- Today's Attendance
- Total Attendance Records
- Students Ready for Face Recognition

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Flask | Web Framework |
| OpenCV | Face Detection |
| face_recognition | Face Recognition |
| SQLite | Database |
| HTML5 | Frontend |
| CSS3 | Styling |
| JavaScript | Client-side Interactions |

---

# 📂 Project Structure

```text
IBM-AI-Based-Smart-Attendance-System/
│
├── database/
│   └── attendance.db
│
├── models/
│   ├── face_trainer.yml
│   └── haarcascade_frontalface_default.xml
│
├── routes/
│   ├── auth_routes.py
│   ├── student_routes.py
│   ├── attendance_routes.py
│   └── camera_routes.py
│
├── static/
│   ├── css/
│   └── images/
│
├── student_images/
│
├── templates/
│
├── utils/
│   ├── capture_faces.py
│   ├── recognize_faces.py
│   └── train_model.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/prerana602/IBM-AI-Based-Smart-Attendance-System.git
```

### 2️⃣ Open the project

```bash
cd IBM-AI-Based-Smart-Attendance-System
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 4️⃣ Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

## Dashboard

<img width="1920" height="1080" alt="dashboard" src="https://github.com/user-attachments/assets/3f3950a6-8471-4c89-86ef-df73f7159831" />


---

## Student Registration

<img width="1920" height="1080" alt="register" src="https://github.com/user-attachments/assets/062cbe91-0ceb-471c-aa52-82ae1fb718c9" />


---

## Student List

<img width="1920" height="1080" alt="students" src="https://github.com/user-attachments/assets/48d1cc0c-2b2f-4164-a6fe-f093a80b0cb7" />


---

## Face Capture

<img width="797" height="626" alt="capture" src="https://github.com/user-attachments/assets/60fe60bc-14c1-4934-a50c-93e441cc42ad" />


---

## Attendance Report

<img width="1920" height="1080" alt="reports" src="https://github.com/user-attachments/assets/af7b9700-5dad-44b8-b68f-3a82f943319f" />


---

# 💡 Workflow

1. Register Student
2. Capture Face Dataset
3. Train Face Recognition Model
4. Recognize Student Face
5. Mark Attendance
6. Generate Attendance Report
7. Export Report as CSV

---

# 📈 Future Improvements

- Email attendance notifications
- QR Code Attendance
- Multiple Camera Support
- Cloud Database Integration
- Mobile Application
- Face Mask Detection
- Admin Authentication
- Attendance Analytics Dashboard
- Attendance Percentage Calculation

---

# 👩‍💻 Developer

**Prerana Verma**

BCA Final Year Student

GitHub: https://github.com/prerana602

---

# 📄 License

This project is developed for educational and learning purposes.
