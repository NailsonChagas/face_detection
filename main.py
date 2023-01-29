import numpy as np
import sqlite3
import cv2

DB_CONNECTION = sqlite3.connect('./db/cv.db')
DB_CURSOR = DB_CONNECTION.cursor()

def setCamera(id, width, height):
    cam = cv2.VideoCapture(id)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    if not cam.isOpened():
        raise IOError("Cannot open webcam")
    return cam

def main():
    WIDTH = 640
    HEIGHT = 480
    background = np.zeros((HEIGHT, WIDTH * 2, 3), dtype=np.uint8) # img null
    cam = setCamera(0, WIDTH, HEIGHT)

    while True:
        ret, frame = cam.read()
        
        background[0:HEIGHT, 0:WIDTH] = frame

        cv2.imshow('WEBCAM', background)

        cv2.waitKey(50)
        if cv2.getWindowProperty('WEBCAM', cv2.WND_PROP_VISIBLE) < 1:
            break

    cam.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    DB_CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            lastAccess TIMESTAMP
    );
    """)
    DB_CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS faces (
            user_id INTEGER,
            encodePath VARCHAR(100),
            FOREIGN KEY(user_id) REFERENCES users(id)
    );
    """)

    main()

    DB_CONNECTION.close()