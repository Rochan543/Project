from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Make sure this is downloaded

def detect_persons(frame):
    results = model(frame)
    boxes = results[0].boxes.xyxy.cpu().numpy() if results[0].boxes else []
    return boxes
