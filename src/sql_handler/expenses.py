from typing import List, Tuple
from sqlite3 import Cursor
from datetime import datetime

def insert(cursor: Cursor, description: str, category_id: int, amount: float, date_time: datetime, observation: str) -> None:
    cursor.execute('''
        INSERT INTO expenses(description, category, amount, date_time, observation)
        VALUES (?, ?, ?, ?, ?)
        ''', (description, category_id, amount, date_time, observation)
    )

def select(cursor: Cursor, start: datetime, end: datetime) -> List[Tuple]:
    cursor.execute("""
        SELECT e.id, e.description, c.name AS category, e.amount, e.date_time, e.observation
        FROM expenses e
        JOIN categories c ON e.category = c.id
        WHERE e.date_time BETWEEN ? AND ?
        ORDER BY date_time ASC
        """, (start, end)
    )
    return cursor.fetchall()

def update(cursor: Cursor, old_category_id: int) -> None:
    cursor.execute('UPDATE expenses SET category = NULL WHERE category = ?', (old_category_id,))
