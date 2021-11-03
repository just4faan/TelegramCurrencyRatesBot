from exchange_repository import ExchangeRepo
from telegram_service import TelegramService
from datetime import datetime as dt

class Controller:
    def __init__(self):
        self.dtime = dt.now()
        print(self.dtime)

        self.exch_repo = ExchangeRepo()
        self.tg = TelegramService(self.exch_repo.all_text)

        print('*'*50)

    def run(self):
        pass
