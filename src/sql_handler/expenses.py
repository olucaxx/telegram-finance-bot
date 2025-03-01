from typing import List, Tuple
from sqlite3 import Cursor
from datetime import datetime

def insert(cursor: Cursor, description: str, category_id: int, amount: float, date_time: datetime, observation: str) -> None:
    cursor.execute('''
        INSERT INTO expenses(description, category, amount, date_time, observation)
        VALUES (?, ?, ?, ?, ?)
        ''', (description, category_id, amount, date_time, observation)
    )

def select(cursor: Cursor, start: datetime = None, end: datetime = None, category: str = None, description: str = None) -> List[Tuple]:
    query = '''
        SELECT e.id, e.description, c.name AS category, e.amount, e.date_time, e.observation
        FROM expenses e
        JOIN categories c ON e.category = c.id
        WHERE 1=1
        '''
    params = []
        
    if start and end:
        query += ' AND e.date_time BETWEEN ? AND ?'
        params.append(start, end)
        
    if category:
        query += ' AND c.name = ?'
        params.append(category)
        
    if description:
        query += ' AND e.descrition = ?'
        params.append(description)
        
    query += ' AND e.is_active = 1 ORDER BY e.date_time ASC'
        
    cursor.execute(query, (params))
    return cursor.fetchall()

def delete(cursor: Cursor, id: int) -> None:
    cursor.execute('UPDATE expenses SET is_active = 0 WHERE id = ?', (id,))
