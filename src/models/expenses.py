import datetime

class Expense:
    def __init__(self, id: int, description: str, category: str, amount: float, date_time: datetime, observation: str) -> None:
        self.id = id
        self.description = description
        self.category = category
        self.amount = amount
        self.date_time = date_time
        self.observation = observation
