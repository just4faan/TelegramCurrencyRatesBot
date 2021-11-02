import sqlite3

class CurrencyDB:
    def __init__(self):
        self.my_db = "all_currencies.db"
        self.json_latest = {'query': {'timestamp': 1635680460, 'base_currency': 'USD'}, 'data': {'JPY': 114.01245, 'CNY': 6.40567, 'CHF': 0.91516, 'CAD': 1.2384, 'MXN': 20.54819, 'INR': 74.91703, 'BRL': 5.63736, 'RUB': 70.86452, 'KRW': 1171.12243, 'IDR': 14165.27255, 'TRY': 9.56361, 'SAR': 3.75087, 'SEK': 8.58828, 'NGN': 410.06819, 'PLN': 3.98485, 'ARS': 99.62225, 'NOK': 8.43371, 'TWD': 27.82536, 'IRR': 42001.005, 'AED': 3.673, 'COP': 3757.57387, 'THB': 33.2909, 'ZAR': 15.24019, 'DKK': 6.43463, 'MYR': 4.13907, 'SGD': 1.34826, 'ILS': 3.16237, 'HKD': 7.77763, 'EGP': 15.6604, 'PHP': 50.50018, 'CLP': 813.2226, 'PKR': 170.38468, 'IQD': 1458.04133, 'DZD': 136.95286, 'KZT': 427.29146, 'QAR': 3.64886, 'CZK': 22.14869, 'PEN': 3.98658, 'RON': 4.2767, 'VND': 22750.30468, 'BDT': 85.41251, 'HUF': 311.20864, 'UAH': 26.26064, 'AOA': 596.80664, 'MAD': 9.08513, 'OMR': 0.38471, 'CUC': 24.00034, 'BYR': 2.00002, 'AZN': 1.69304, 'LKR': 200.00466, 'SDG': 438.97762, 'SYP': 2511.04639, 'MMK': 1720.03981, 'DOP': 56.2907, 'UZS': 10669.30822, 'KES': 111.20155, 'GTQ': 7.72515, 'URY': 43.95084, 'HRV': 6.48764, 'MOP': 8.01211, 'ETB': 47.21897, 'CRC': 635.16425, 'TZS': 2300.04364, 'TMT': 3.49009, 'TND': 2.81416, 'PAB': 1.00002, 'LBP': 1505.53515, 'RSD': 101.54156, 'LYD': 4.53958, 'GHS': 6.00017, 'YER': 250.05355, 'BOB': 6.83017, 'BHD': 0.37701, 'CDF': 1992.12338, 'PYG': 6894.17457, 'UGX': 3551.5579, 'SVC': 8.75003, 'TTD': 6.73113, 'AFN': 90.64237, 'NPR': 119.80176, 'HNL': 24.06427, 'BIH': 1.69193, 'BND': 1.34882, 'ISK': 129.64232, 'KHR': 4056.05753, 'GEL': 3.13456, 'MZN': 63.20181, 'BWP': 11.38651, 'PGK': 3.51127, 'JMD': 152.95351, 'XAF': 567.36015, 'NAD': 15.20822, 'ALL': 105.98314, 'SSP': 390.00746, 'MUR': 42.90122, 'MNT': 2837.04264, 'NIO': 35.21038, 'LAK': 10295.20676, 'MKD': 52.97141, 'AMD': 474.21057, 'MGA': 3957.10061, 'XPF': 102.9324, 'TJS': 11.24034, 'HTG': 96.72281, 'BSD': 1.00002, 'MDL': 17.35944, 'RWF': 1017.52904, 'KGS': 84.80135, 'GNF': 9550.23626, 'SRD': 21.39562, 'SLL': 10779.1825, 'XOF': 558.75939, 'MWK': 807.36981, 'FJD': 2.06412, 'ERN': 15.00026, 'SZL': 15.23763, 'GYD': 208.19478, 'BIF': 1979.02831, 'KYD': 0.82502, 'MVR': 15.42024, 'LSL': 15.23288, 'LRD': 150.50177, 'CVE': 95.36271, 'DJF': 177.50381, 'SCR': 14.35879, 'SOS': 575.0158, 'GMD': 52.15123, 'KMF': 423.04942, 'STD': 21.20063, 'XRP': 0.93002, 'AUD': 1.32983, 'BGN': 1.69143, 'BTC': 0.016, 'JOD': 0.70802, 'GBP': 0.73032, 'ETH': 0.00023, 'EUR': 0.86493, 'LTC': 0.01, 'NZD': 1.39552}}
        self.timestamp = self.json_latest['query']['timestamp']
        self.base_currency = self.json_latest['query']['base_currency']

    def create(self):
        conn = sqlite3.connect(self.my_db)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS latest_currencies(
                        id INTEGER PRIMARY KEY AUTOINCREMENT ,
                        currencies TEXT,
                        rates TEXT,
                        time_rates TEXT,
                        base_currency TEXT);""")
        query = """INSERT INTO latest_currencies
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
            print(row)
        conn.close()

    def read_specific_columns(self, col_list):
        conn = sqlite3.connect(self.my_db)
        cur = conn.cursor()
        columns = ", ".join(col_list)
        query = f"SELECT {columns} FROM latest_currencies;"
        cur.execute(query)
        results = cur.fetchall()
        for row in results:
            yield row
            print(row)
        conn.close()

    def drop_latest_table(self):
        conn = sqlite3.connect(self.my_db)
        cur = conn.cursor()
        query = "DROP TABLE IF EXISTS latest_currencies;"
        cur.execute(query)
        conn.commit()
        conn.close()

    def update(self):
        pass

    def delete(self):
        pass

if __name__ == '__main__':
    curr_db = CurrencyDB()
    # curr_db.create()
    # curr_db.read()
    curr_db.read_specific_columns(['id', 'currencies', 'rates', 'time_rates', 'base_currency'])
    # curr_db.drop_latest_table()
    # for k,v in curr_db.json_latest['data'].items():
    #     print(k,' : ',v)
