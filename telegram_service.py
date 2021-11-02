import telebot
import sqlite3


class TelegramService():
    __TOKEN = 'YOUR_TOKEN'
    TIMEZONE = 'Europe/Kiev'
    TIMEZONE_COMMON_NAME = 'Kiev'
    my_db = "all_currencies.db"
    conn = sqlite3.connect(my_db)
    cur = conn.cursor()
    d_latest = {
        "query": {"apikey": "87e07f20-3508-11ec-9594-63b97110f843", "timestamp": 1635326935, "base_currency": "USD"},
        "data": {"JPY": 113.67164, "CNY": 6.3929, "CHF": 0.918, "CAD": 1.24184, "MXN": 20.23089, "INR": 75.03132,
                 "BRL": 5.56654, "RUB": 70.02564, "KRW": 1169.2177, "IDR": 14170.14455, "TRY": 9.49581, "SAR": 3.75025,
                 "SEK": 8.61763, "NGN": 409.99622, "PLN": 3.98045, "ARS": 99.5428, "NOK": 8.40669, "TWD": 27.82544,
                 "IRR": 42000.73659, "AED": 3.67265, "COP": 3769.10987, "THB": 33.34038, "ZAR": 14.98667,
                 "DKK": 6.41511, "MYR": 4.15111, "SGD": 1.34949, "ILS": 3.19208, "HKD": 7.77823, "EGP": 15.73208,
                 "PHP": 50.74967, "CLP": 803.69214, "PKR": 172.0538, "IQD": 1458.02081, "DZD": 136.44248,
                 "KZT": 426.63466, "QAR": 3.64004, "CZK": 22.16363, "PEN": 3.97521, "RON": 4.26509, "VND": 22745.48123,
                 "BDT": 85.60178, "HUF": 314.97436, "UAH": 26.36052, "AOA": 597.01101, "MAD": 9.06717, "OMR": 0.38501,
                 "CUC": 24.00064, "BYR": 2.00005, "AZN": 1.69502, "LKR": 200.00571, "SDG": 438.97467, "SYP": 2511.02927,
                 "MMK": 1770.04889, "DOP": 56.25119, "UZS": 10662.24987, "KES": 111.00298, "GTQ": 7.72918,
                 "URY": 43.67131, "HRV": 6.48036, "MOP": 8.01123, "ETB": 47.10604, "CRC": 629.11629, "TZS": 2295.05221,
                 "TMT": 3.49008, "TND": 2.82565, "PAB": 1.00003, "LBP": 1505.71624, "RSD": 101.27118, "LYD": 4.53847,
                 "GHS": 5.90015, "YER": 250.00729, "BOB": 6.82016, "BHD": 0.37701, "CDF": 1980.62923, "PYG": 6917.90233,
                 "UGX": 3549.10643, "SVC": 8.74967, "TTD": 6.74949, "AFN": 90.34206, "NPR": 119.98195, "HNL": 24.05229,
                 "BIH": 1.68545, "BND": 1.34933, "ISK": 129.21141, "KHR": 4060.07264, "GEL": 3.12007, "MZN": 62.20167,
                 "BWP": 11.31759, "PGK": 3.51124, "JMD": 153.27232, "XAF": 565.69343, "NAD": 14.98526, "ALL": 105.30213,
                 "SSP": 390.01157, "MUR": 43.05052, "MNT": 2825.04104, "NIO": 35.2106, "LAK": 10210.12525,
                 "MKD": 53.04135, "AMD": 474.00749, "MGA": 3965.04066, "XPF": 102.63113, "TJS": 11.23013,
                 "HTG": 99.00198, "BSD": 1.00002, "MDL": 17.45037, "RWF": 1017.02294, "KGS": 84.79148,
                 "GNF": 9580.28573, "SRD": 21.38949, "SLL": 10670.19739, "XOF": 568.1262, "MWK": 807.53041,
                 "FJD": 2.07093, "ERN": 15.00044, "SZL": 14.98131, "GYD": 207.98398, "BIF": 1979.02882, "KYD": 0.82502,
                 "MVR": 15.42041, "LSL": 14.98516, "LRD": 151.30173, "CVE": 95.09169, "DJF": 177.50203, "SCR": 13.44115,
                 "SOS": 575.01366, "GMD": 52.10153, "KMF": 423.36031, "STD": 21.12048, "XRP": 0.88002, "AUD": 1.33343,
                 "BGN": 1.68662, "BTC": 0.0164, "JOD": 0.70801, "GBP": 0.72642, "ETH": 0.00023, "EUR": 0.86242,
                 "LTC": 0.01, "NZD": 1.39622}}
    selection = cur.execute("SELECT currencies, rates, time_rates FROM latest_currencies ORDER BY rates;")
    # selection = cur.execute("SELECT * FROM my_data ORDER BY rates;")
    sel = cur.fetchall()
    text = ''
    # for row in sel:
    #     text += f"{row[0]}: {row[1]}\n"
    # print(text)

    def bot_start(self):
        bot = telebot.TeleBot(TelegramService.__TOKEN)

        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.send_message(message.chat.id, "Welcome to the club, buddy!")

        @bot.message_handler(commands=['help'])
        def help_command(message):
            bot.send_message(message.chat.id, 'This is exchange currency bot')

        @bot.message_handler(commands=['list', 'lst'])
        def get_exchange(message):
            bot.send_message(message.chat.id, TelegramService.text)

        @bot.message_handler(commands=['kek'])
        def long_message(message):
            for i in TelegramService.sel:
                if message.text == i[0]:
                    bot.send_message(message.chat.id, f"{i[0]} -> {i[1]}")
            for i in TelegramService.sel:
                if message.text == '/kek {}'.format(i[0]):
                    print(i)
                    bot.send_message(message.chat.id, f"{i[0]} -> {i[1]}")

        bot.infinity_polling()


# if __name__ == '__main__':
#     tg = TelegramService()
#     tg.bot_start()
