# ----------------------------- app/recognizer.py -----------------------------
import os
import cv2
import numpy as np
from deepface import DeepFace

def recognize_face(face_img, db_path="face_db"):
    try:
        temp_path = "temp_face.jpg"
        cv2.imwrite(temp_path, face_img)
        result = DeepFace.find(img_path=temp_path, db_path=db_path, enforce_detection=False)
        os.remove(temp_path)
        if not result[0].empty:
            identity = os.path.basename(result[0].iloc[0]["identity"])
            return identity.split('.')[0]
    except Exception:
        pass
    return "Unknown"
