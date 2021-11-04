
from web_service import WebService
from database import CurrencyDB


class ExchangeRepo:
    def __init__(self):
        self.curr_db = CurrencyDB()
        self.ws = WebService()

        self.curr_db.json_latest = self.ws.get_latest_json_currencies()
        self.curr_db.create()
        self.curr_db.read()

        # self.curr_db.update()
        # self.curr_db.drop_latest_table()

        # SELECT all data
        # self.currencies_rates_all = self.curr_db.read()

        # SELECT specific data: currencies and rates
        self.currencies_rates_specific = self.curr_db.read_specific_columns(['currencies', 'rates'])

        # all currencies and rates in string variable
        self.all_text = ""
        for k in self.currencies_rates_specific:
            # print(k[0], '->', k[1])
            self.all_text += f"{k[0]} -> {k[1]}\n"
        print(self.all_text)




if __name__ == '__main__':
    pass
