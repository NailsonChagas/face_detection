import sqlite3
import cv2

DB_CONNECTION = sqlite3.connect('./db/cv.db')
DB_CURSOR = DB_CONNECTION.cursor()

def main():
    cam = cv2.VideoCapture(0)
    width = 500
    height = 500
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    if not cam.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cam.read()
        cv2.imshow('WEBCAM', frame)

        c = cv2.waitKey(1)
        if c == 27:
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