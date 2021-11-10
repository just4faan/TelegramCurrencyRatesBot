import threading

import telebot

import sqlite3
import time
import re
from threading import Thread


class TelegramService:
    def __init__(self, currencies_rates_text, curr_rates_list):
        # self.__TOKEN = 'YOUR_TOKEN'
        self.TIMEZONE = 'Europe/Kiev'
        self.TIMEZONE_COMMON_NAME = 'Kiev'
        self.bot = telebot.TeleBot(self.__TOKEN)
        self.currencies_rates_text = currencies_rates_text
        self.curr_rates_list = curr_rates_list
        print(threading.get_ident())

        @self.bot.message_handler(commands=['start'])
        def _send_welcome(message):
            self.send_welcome(message)

        @self.bot.message_handler(commands=['help'])
        def _help_command(message):
            self.help_command(message)

        @self.bot.message_handler(commands=['list', 'lst'])
        def _get_currencies_rates(message):
            self.get_currencies_rates(message)
            
        # @self.bot.message_handler(regexp=["^(/exchange [$]([0-9]+) to ([A-Z]{3,3})|/exchange ([0-9]+) USD to ([A-Z]{3,3}))$"])
        @self.bot.message_handler(regexp='/exchange')
        def _get_currency_exchange(message):
            self.get_currency_exchange(message)
        
        @self.bot.message_handler(commands=['history'])
        def _get_history(message):
            self.get_history(message)

        # self.bot.infinity_polling()

    def run_bot(self):
        self.bot.infinity_polling()

    @property
    def currencies_rates_text(self):
        print("Getting value")
        return self._currencies_rates_text

    @currencies_rates_text.setter
    def currencies_rates_text(self, text):
        print("Setting value")
        self._currencies_rates_text = text

    # def validate_exchange(self, message):
    #     self.bot.reply_to('validation')

    def send_welcome(self, message):
        self.bot.send_message(message.chat.id, "Welcome to the club, buddy!")
        self.bot.send_message(message.chat.id, 'Welcome, '+str(message.from_user.first_name))

    def help_command(self, message):
        self.bot.send_message(message.chat.id, 'This is exchange currency bot')

    def get_currencies_rates(self, message):
        self.bot.send_message(message.chat.id, self.currencies_rates_text)

    def get_currency_exchange(self, message):
        exchange_currencies = re.compile(
            "^(/exchange [$]([0-9]+) to ([A-Z]{3,3})|/exchange ([0-9]+) USD to ([A-Z]{3,3}))$")
        curr_search = exchange_currencies.search(message.text)
        if curr_search is not None:
            result = ""
            clean = list(filter(None, curr_search.groups()))
            usd_to_curr = self.convert_usd_to_currency(clean)
            if usd_to_curr:
                result += str(usd_to_curr)
            else: result = "Wrong exchange input, rerun command and try again"
            # print(usd_to_curr)
            # print(clean)
        else: result = "Wrong exchange input, rerun command and try again"
        self.bot.send_message(message.chat.id, result)

    def convert_usd_to_currency(self, convert: list):
        amount_usd = convert[1]
        check_curr = convert[2]
        exchange_rate = 0
        for curr, rate in self.curr_rates_list:
            if curr == check_curr:
                print(curr, ' : ', rate)
                exchange_rate = rate * float(amount_usd)
        return exchange_rate

    def get_history(self, message):
        self.bot.send_message(message.chat.id, 'hiiistory')

        # @bot.message_handler(commands=['kek'])
        # def long_message(message):
        #     for i in TelegramService.sel:
        #         if message.text == i[0]:
        #             bot.send_message(message.chat.id, f"{i[0]} -> {i[1]}")
        #     for i in TelegramService.sel:
        #         if message.text == '/kek {}'.format(i[0]):
        #             print(i)
        #             bot.send_message(message.chat.id, f"{i[0]} -> {i[1]}")


if __name__ == '__main__':
    tg = TelegramService()
