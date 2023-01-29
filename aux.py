import cv2

def setCamera(id, width, height):
    cam = cv2.VideoCapture(id)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    if not cam.isOpened():
        raise IOError("Cannot open webcam")
    return cam

def text(img, string, scale, position):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(
        img, string, position, 
        font, scale, (255,255,255)
    )