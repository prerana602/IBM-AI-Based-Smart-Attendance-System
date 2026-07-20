from datetime import datetime
import cv2
import sqlite3

# Load face detector
face_detector = cv2.CascadeClassifier(
    "models/haarcascade_frontalface_default.xml"
)

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("models/face_trainer.yml")

# Open database
conn = sqlite3.connect("database/attendance.db")
cursor = conn.cursor()

# Start webcam
camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        student_id, confidence = recognizer.predict(face)

        cursor.execute(
            "SELECT name FROM students WHERE student_id=?",
            (str(student_id),)
        )

        result = cursor.fetchone()

        if result and confidence < 80:

            name = result[0]

            today = datetime.now().strftime("%Y-%m-%d")
            current_time = datetime.now().strftime("%H:%M:%S")

            cursor.execute("""
                SELECT * FROM attendance
                WHERE student_id=? AND date=?
            """, (str(student_id), today))

            already_marked = cursor.fetchone()

            if not already_marked:

                cursor.execute("""
                    INSERT INTO attendance
                    (student_id, name, date, time, status)

                    VALUES (?, ?, ?, ?, ?)
                """,
                (
                    str(student_id),
                    name,
                    today,
                    current_time,
                    "Present"
                ))

                conn.commit()

                text = f"{name} - Attendance Marked"

            else:

                text = f"{name} - Already Marked"

            color = (0, 255, 0)

        else:

            text = "Unknown"
            color = (0, 0, 255)

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            color,
            2
        )

        cv2.putText(
            frame,
            text,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

    cv2.imshow("AI Attendance System", frame)

    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
conn.close()
cv2.destroyAllWindows()