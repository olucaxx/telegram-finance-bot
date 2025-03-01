from datetime import datetime
from typing import List, Tuple
from data.repositories import categories, expenses, execute_query

### CATEGORIES HANDLERS

def insert_into_categories(category_name: str) -> None:
    category_name = category_name
    
    try: 
        # verifica se já existe uma categoria com esse nome que está com o atributo is_active = 0, 
        # se houver, reativa ela e finaliza. caso não tenha, irá gerar uma exceção, caindo no except propositalmente e executando o insert
        select_from_categories(category_name, False)[0][0] 
        execute_query(categories.reactivate, category_name)
        return
    
    except (IndexError, TypeError): # IndexError é pelo motivo comentado acima, TypeError é quando não temos NENHUMA categoria inserida
        execute_query(categories.insert, category_name)
    
    
def select_from_categories(category: str | None = None, check_if_active: bool = True) -> List[Tuple]:
    return execute_query(categories.select, category, check_if_active)


def deactivate_from_categories(category: str) -> None:
    execute_query(categories.deactivate, category)

### EXPENSES HANDLERS

def insert_into_expenses(description: str, category: str, amount: float, date_time: datetime, observation: str = "Sem observação") -> None:
    category_name = category

    # bloco try-excecpt pagar pegar o id da categoria através do nome que foi passado
    try:
        category_id = select_from_categories(category_name)[0][0] # verifica se a categoria já existe, se não existir, gera IndexError
    except IndexError:
        insert_into_categories(category_name) 
        category_id = select_from_categories(category_name)[0][0] 
    
    execute_query(expenses.insert, description, category_id, amount, date_time, observation)


def select_from_expenses(start: datetime = None, end: datetime = None, category: str = None, description: str = None) -> List[Tuple]:
    return execute_query(expenses.select, start, end, category, description)


def deactivate_from_expenses(id: int) -> None:
    execute_query(expenses.deactivate, id)
