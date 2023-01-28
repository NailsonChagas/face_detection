import sqlite3
DB_CONNECTION = sqlite3.connect('./db/users.db')
DB_CURSOR = DB_CONNECTION.cursor()

def main():
    pass

if __name__ == "__main__":
    DB_CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ultimoAcesso DATETIME
    );
    """)
    main()
    DB_CONNECTION.close()