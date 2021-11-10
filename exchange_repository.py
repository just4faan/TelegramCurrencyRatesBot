import time
import threading
from threading import Thread
from web_service import WebService
from database import CurrencyDB
from datetime import datetime as dt

class ExchangeRepo:
    def __init__(self):
        self.dtime = dt.now()
        print(self.dtime)

        self.curr_db = CurrencyDB()
        self.ws = WebService()

        # self.curr_db.json_latest = self.ws.get_latest_json_currencies()
        # self.curr_db.create()

        # self.curr_db.update()
        # self.curr_db.drop_latest_table()

        # all currencies and rates in string variable
        self.text_curr_rates = self.curr_db.read_specific_columns(['currencies', 'rates'])
        self.curr_rates_generator = self.curr_db.read_specific_columns(['currencies', 'rates'])
        print(self.text_curr_rates)

    @property
    def text_curr_rates(self):
        return self._text_curr_rates

    @text_curr_rates.setter
    def text_curr_rates(self, curr_rates_columns):
        text = ''

        for k in curr_rates_columns:
            text += f"{k[0]} -> {k[1]}\n"
        # print(text)
        self._text_curr_rates = text

    # Every 10 minutes request from currency API and update db
    def request_every_ten_minutes(self):
        while True:
            time.sleep(60000)
            print("Updating db with json data...")
            print(threading.get_ident())
            self.curr_db.json_latest = self.ws.get_latest_json_currencies()
            self.curr_db.update()
            self.text_curr_rates = self.curr_db.read_specific_columns(['currencies', 'rates'])


if __name__ == '__main__':
    pass
