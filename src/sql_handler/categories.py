from typing import List, Tuple
from sqlite3 import Cursor

def insert(cursor: Cursor, name: str) -> None:
    cursor.execute('INSERT INTO categories(name) VALUES (?)', (name,))

def select(cursor: Cursor, category: str | None = None, check_existense: bool = True) -> List[Tuple]:
    query = 'SELECT id, name FROM categories WHERE 1=1'
    params = []
    
    if category:
        query += ' AND name = ?'
        params.append(category)
    
    if check_existense:
        query += ' AND is_active = 1'
        
    query += ' ORDER BY id ASC'
    
    cursor.execute(query, (params))
    return cursor.fetchall()

def deactivate(cursor: Cursor, name: str) -> None:
    cursor.execute('UPDATE categories SET is_active = 0 WHERE name = ?', (name,))
    
def reactivate(cursor: Cursor, name: str) -> None:
    cursor.execute('UPDATE categories SET is_active = 1 WHERE name = ?', (name,))