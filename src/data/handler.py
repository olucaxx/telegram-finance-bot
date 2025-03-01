import sqlite3
from datetime import datetime
from typing import Callable, List, Tuple
from sql_handler import categories, expenses, initializer
from utils import prep_str

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

### CATEGORIES HANDLERS

def insert_into_categories(category_name: str) -> None:
    category_name = prep_str(category_name)
    
    try: 
        print(select_from_categories(category_name, False)[0][0])
        execute_query(categories.reactivate, category_name)
        return
    except (IndexError, TypeError) as e: 
        print(e)
        pass
    
    execute_query(categories.insert, category_name)
    
def select_from_categories(category: str | None = None, check_existense: bool = True) -> List[Tuple]:
    return execute_query(categories.select, prep_str(category), check_existense)

def deactivate_from_categories(category: str) -> None:
    execute_query(categories.deactivate, prep_str(category))

### EXPENSES HANDLERS

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