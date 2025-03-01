import sqlite3
from sqlite3 import Cursor
from typing import Callable

PATH = 'src/data/records.db'

def execute_query(func: Callable, *args, **kwargs) -> None:
    '''função para executar as queries, recebe a query como argumento através da 'func' e faz uma coneção com with no banco de dados'''
    try:
        with sqlite3.connect(PATH) as con:
            result = func(con.cursor(), *args, **kwargs)
            con.commit()
            return result
    
    except sqlite3.Error as e:
        print(f"unexpected error: {e}")
        con.rollback() # tenta previnir danos voltando atrás com as mudanças caso ocorram erros
        return None
        

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
            observation TEXT NOT NULL,
            is_active INTEGER DEFAULT 1 CHECK (is_active IN (0, 1)),
            FOREIGN KEY (category) REFERENCES categories(id)
        )'''
    )


execute_query(initializer)