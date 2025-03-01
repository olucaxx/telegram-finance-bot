import data.handler
import datetime

description = "Compra de alimentos"
category = "Transporte"
amount = 45.99
date_time = datetime.datetime(2023, 2, 28, 18, 30, 0)
date_time1 = datetime.datetime(2025, 2, 28, 18, 30, 0)
observation = "Compra de mercado"


data.handler.create_tables()
data.handler.insert_into_categories("AlimenTação")
data.handler.insert_into_categories(" saúdE")
data.handler.insert_into_categories("TRANSPORTE")
data.handler.insert_into_categories("contas ")