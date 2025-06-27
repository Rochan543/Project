from deepface import DeepFace

def analyze_emotion(face_img):
    try:
        analysis = DeepFace.analyze(face_img, actions=['emotion'], enforce_detection=False)
        if isinstance(analysis, list):
            return analysis[0]['dominant_emotion']
        return analysis['dominant_emotion']
    except:
        return "N/A"