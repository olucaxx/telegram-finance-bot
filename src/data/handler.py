import sqlite3
from datetime import datetime
from typing import Callable, List, Tuple
from sql_handler import categories, expenses, initializer

PATH = 'src/data/records.db'

def execute_query(func: Callable, *args, **kwargs) -> None:
    try:
        with sqlite3.connect(PATH) as con:
            result = func(con.cursor(), *args, **kwargs)
            con.commit()
            return result
    
    except sqlite3.Error as e:
        print(f"unexpected error: {e}")
        con.rollback()
        return None
        
def create_tables() -> None:
    execute_query(initializer)

def insert_into_categories(category: str) -> None:
    execute_query(categories.insert, category)

def delete_from_categories(category: str) -> None:
    category_id = select_from_categories(category)[0][0]
    execute_query(expenses.update, category_id)
    execute_query(categories.delete, category)
    
def select_from_categories(category: str | None = None) -> List[Tuple]:
    return execute_query(categories.select, category)

def insert_into_expenses(description: str, category: int, amount: float, date_time: datetime, observation: str) -> None:
    try:
        category_id = select_from_categories(category)[0][0]
    except IndexError:
        insert_into_categories(category)
        category_id = select_from_categories(category)[0][0]
    
    execute_query(expenses.insert, description, category_id, amount, date_time, observation)

def select_from_expenses(start: datetime, end: datetime) -> List[Tuple]:
    return execute_query(expenses.select, start, end)


create_tables()