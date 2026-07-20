import os
import cv2
import numpy as np

# Create LBPH recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []

dataset_path = "student_images"

# Read every student's folder
for student_folder in os.listdir(dataset_path):

    folder_path = os.path.join(dataset_path, student_folder)

    if not os.path.isdir(folder_path):
        continue

    label = int(student_folder)

    for image_name in os.listdir(folder_path):

        image_path = os.path.join(folder_path, image_name)

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            continue

        faces.append(image)
        labels.append(label)

labels = np.array(labels)

print("Training Started...")
print(f"Total Images : {len(faces)}")
print(f"Students : {len(set(labels))}")

recognizer.train(faces, labels)

recognizer.save("models/face_trainer.yml")

print("Training Completed Successfully!")
print("Model saved as models/face_trainer.yml")