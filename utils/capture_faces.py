import cv2
import os
import sys

# Get Student ID from command line

if len(sys.argv) < 2:
    print("Student ID not provided.")
    sys.exit()

student_id = sys.argv[1]

# Create folder for this student
folder_path = os.path.join("student_images", student_id)
os.makedirs(folder_path, exist_ok=True)

# Load face detector
face_detector = cv2.CascadeClassifier(
    "models/haarcascade_frontalface_default.xml"
)

# Start webcam
camera = cv2.VideoCapture(0)

count = 0

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

        count += 1

        face = gray[y:y+h, x:x+w]

        face = cv2.resize(face, (200, 200))

        filename = os.path.join(folder_path, f"{count}.jpg")

        cv2.imwrite(filename, face)

        cv2.rectangle(frame,
                      (x, y),
                      (x+w, y+h),
                      (0, 255, 0),
                      2)

        cv2.putText(
            frame,
            f"Images: {count}/100",
            (20, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

    cv2.imshow("Capture Faces", frame)

    if cv2.waitKey(1) == ord("q"):
        break

    if count >= 100:
        break

camera.release()
cv2.destroyAllWindows()

print("Face dataset created successfully!")