from typing import List, Tuple
from sqlite3 import Cursor

def insert(cursor: Cursor, name: str) -> None:
    cursor.execute('INSERT INTO categories(name) VALUES (?)', (name,))

def delete(cursor: Cursor, name: str) -> None:
    cursor.execute('DELETE FROM categories WHERE name = ?', (name,))
    
def select(cursor: Cursor, category: str | None = None) -> List[Tuple]:
    if category != None:
        cursor.execute('SELECT * FROM categories WHERE name = ?', (category,))
        return cursor.fetchall()
    
    cursor.execute('SELECT * FROM categories')
    return cursor.fetchall()
