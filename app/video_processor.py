import cv2

def get_video_stream(source=0):
    return cv2.VideoCapture(source)

def read_frame(cap):
    ret, frame = cap.read()
    return frame if ret else None

def release_stream(cap):
    cap.release()
    cv2.destroyAllWindows()
