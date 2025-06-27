import cv2
from app.video_processor import get_video_stream, read_frame, release_stream
from app.detector import detect_persons
from app.recognizer import recognize_face
from app.emotion import analyze_emotion
from app.logger import log_data

cap = get_video_stream(0)

while True:
    frame = read_frame(cap)
    if frame is None:
        break

    boxes = detect_persons(frame)

    for box in boxes:
        x1, y1, x2, y2 = map(int, box)
        face = frame[y1:y2, x1:x2]
        name = recognize_face(face)
        emotion = analyze_emotion(face)

        log_data(name, emotion)

        label = f"{name}, {emotion}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Live Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

release_stream(cap)
