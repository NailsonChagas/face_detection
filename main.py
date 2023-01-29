import sqlite3

DB_CONNECTION = sqlite3.connect('./db/cv.db')
DB_CURSOR = DB_CONNECTION.cursor()

def main():
    pass

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
            imagePath VARCHAR(100),
            FOREIGN KEY(user_id) REFERENCES users(id)
    );
    """)

    main()
    
    DB_CONNECTION.close()