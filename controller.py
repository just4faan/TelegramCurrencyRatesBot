import time
from threading import Thread
from exchange_repository import ExchangeRepo
from telegram_service import TelegramService



class Controller:
    def __init__(self):
        t1 = Thread(target=self.main_flow)
        t2 = Thread(target=self.exch_repo.request_every_ten_minutes())

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print('*'*50)

    def main_flow(self):
        self.exch_repo = ExchangeRepo()
        self.tg = TelegramService(self.exch_repo.text_curr_rates)
        time.sleep(2)
