import os
from typing import Final
'''the name "TELEGRAM_BOT_TOKEN" should be the name of the sys variable that has the token key assigned'''
TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN").strip()
