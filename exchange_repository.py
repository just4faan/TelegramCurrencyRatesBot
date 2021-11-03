
from web_service import WebService
from database import CurrencyDB


class ExchangeRepo():
    def __init__(self):
        self.curr_db = CurrencyDB()
        self.ws = WebService()

        # self.curr_db.json_latest = self.ws.get_latest_json_currencies()
        # self.curr_db.create()
        self.curr_db.read()
        # self.curr_db.drop_latest_table()


if __name__ == '__main__':
    pass
