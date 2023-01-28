import sqlite3
DB_CONNECTION = sqlite3.connect('./db/users.db')

def main():
    pass

if __name__ == "__main__":
    main()
    DB_CONNECTION.close()