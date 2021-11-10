import time
import threading
from threading import Thread, Timer
from exchange_repository import ExchangeRepo
from telegram_service import TelegramService

from concurrent.futures import ThreadPoolExecutor


class Controller:
    def __init__(self):
        self.exch_repo = ExchangeRepo()
        self.tg = TelegramService(self.exch_repo.text_curr_rates, self.exch_repo.curr_rates_list)

        print(threading.get_ident())

        t1 = Thread(target=self.tg.run_bot, daemon=True)
        t2 = Thread(target=self.exch_repo.request_every_ten_minutes, daemon=True)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        # with ThreadPoolExecutor(max_workers=2) as executor:
        #     print(threading.get_ident())
        #     executor.submit(self.exch_repo.request_every_ten_minutes)
        #     executor.submit(self.tg.run_bot).result()

            # t1.result()











