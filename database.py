import sqlite3


class CurrencyDB:
    def __init__(self):
        self.json_latest = None

        self.my_db = "all_currencies.db"


    def create(self):
        self.timestamp = self.json_latest['query']['timestamp']
        self.base_currency = self.json_latest['query']['base_currency']

        conn = sqlite3.connect(self.my_db)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS latest_currencies(
                        id INTEGER PRIMARY KEY AUTOINCREMENT ,
                        currencies TEXT UNIQUE,
                        rates FLOAT,
                        time_rates TEXT,
                        base_currency TEXT);""")
        query = """INSERT OR IGNORE INTO latest_currencies
                            (currencies, rates, time_rates, base_currency) VALUES
                            (?, ?, ?, ?);"""
        for currency, rate in self.json_latest['data'].items():
            cur.execute(query, (currency, rate, self.timestamp, self.base_currency))
        conn.commit()
        conn.close()

    def read(self):
        conn = sqlite3.connect(self.my_db)
        cur = conn.cursor()
        query = "SELECT * FROM latest_currencies;"
        cur.execute(query)
        results = cur.fetchall()
        for row in results:
            yield row
        conn.close()

    def read_specific_columns(self, col_list):
        conn = sqlite3.connect(self.my_db)
        cur = conn.cursor()
        columns = ", ".join(col_list)
        query = f"SELECT {columns} FROM latest_currencies ORDER BY rates;"
        cur.execute(query)
        results = cur.fetchall()
        for row in results:
            yield row
            # print(row)
        conn.close()

    def drop_latest_table(self):
        conn = sqlite3.connect(self.my_db)
        cur = conn.cursor()
        query = "DROP TABLE IF EXISTS latest_currencies;"
        cur.execute(query)
        conn.commit()
        conn.close()

    def update(self):
        print(self.json_latest)
        self.timestamp = self.json_latest['query']['timestamp']
        self.base_currency = self.json_latest['query']['base_currency']
        try:
            conn = sqlite3.connect(self.my_db)
            cur = conn.cursor()
            print("Connected to SQLite")

            # query = """UPDATE latest_currencies SET (currencies, rates, time_rates, base_currency) = (?, ?, ?, ?);"""
            query = """REPLACE INTO latest_currencies
                                        (currencies, rates, time_rates, base_currency) VALUES
                                        (?, ?, ?, ?);"""
            for currency, rate in self.json_latest['data'].items():
                cur.execute(query, (currency, rate, self.timestamp, self.base_currency))
            conn.commit()
            print("Record Updated successfully ")
            cur.close()

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")

    def delete(self):
        pass

if __name__ == '__main__':
    curr_db = CurrencyDB()
    # curr_db.create()
    # curr_db.read()
    curr_db.read_specific_columns(['id', 'currencies', 'rates', 'time_rates', 'base_currency'])
    curr_db.drop_latest_table()
    # for k,v in curr_db.json_latest['data'].items():
    #     print(k,' : ',v)
