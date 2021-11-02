
from web_service import WebService
from database import CurrencyDB


class ExchangeRepo():
    def __init__(self):
        self.curr_db = CurrencyDB()
        self.ws = WebService()
        self.kek = 'real kek'
        print(self.kek)
