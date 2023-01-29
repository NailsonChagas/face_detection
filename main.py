from aux import setCamera, text
import numpy as np
import cv2

def main():
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

    DELAY = 25/1000 #s
    WIDTH = 640
    HEIGHT = 480
    cam = setCamera(0, WIDTH, HEIGHT)
    frames = 0

    while True:
        background = np.zeros((HEIGHT, WIDTH * 2, 3), dtype=np.uint8) # img null

        ret, frame = cam.read()
        dimensions = (frame.shape[1], frame.shape[0])
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale(gray, scaleFactor =1.2, minNeighbors=4) #detectando rostos
        
        for (x, y, w, h) in faces:
            regionOfInterest = frame[y:y+h, x:x+w]
            resized = cv2.resize(regionOfInterest, dimensions, interpolation=cv2.INTER_AREA)
            background[0:HEIGHT, WIDTH:] = resized
            color = (255, 0, 0)
            stroke = 2
            cv2.rectangle(frame, (x, y), (w + x, h + y), color, stroke)
            
        background[0:HEIGHT, 0:WIDTH] = frame

        text(background, f"FRAME COUNT: {frames} / FPS: {1/DELAY}", 1/2, (WIDTH, 15))
        cv2.imshow("WEBCAM", background)

        frames += 1
        cv2.waitKey(int(DELAY*1000)) #ms
        if cv2.getWindowProperty("WEBCAM", cv2.WND_PROP_VISIBLE) < 1:
            break

    cam.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()