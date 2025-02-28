import datetime

class Expense:
    def __init__(self) -> None:
        self.id: int
        self.description: str
        self.category: int
        self.amount: float
        self.date_time: datetime
        self.observation: str
