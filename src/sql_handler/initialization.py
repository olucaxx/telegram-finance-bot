from sqlite3 import Cursor

def initializer(cursor: Cursor):
    cursor.execute('''        
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL
        )'''
    )
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description VARCHAR(255) NOT NULL,
            category INT, 
            amount DECIMAL(10, 2) NOT NULL,
            date_time DATETIME NOT NULL,
            observation TEXT,
            FOREIGN KEY (category) REFERENCES categories(id)
        )'''
    )