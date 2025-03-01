from sqlite3 import Cursor

def initializer(cursor: Cursor):
    cursor.execute('''        
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            is_active INTEGER DEFAULT 1 CHECK (is_active IN (0, 1))
        )'''
    )
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            category INTEGER NOT NULL, 
            amount REAL NOT NULL,
            date_time TEXT NOT NULL,
            observation TEXT,
            is_active INTEGER DEFAULT 1 CHECK (is_active IN (0, 1)),
            FOREIGN KEY (category) REFERENCES categories(id)
        )'''
    )
    