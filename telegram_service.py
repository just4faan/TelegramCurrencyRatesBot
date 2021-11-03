import telebot
import sqlite3


class TelegramService:
    def __init__(self, currencies_rates_text):
        self.__TOKEN = 'YOUR_TOKEN'
        self.TIMEZONE = 'Europe/Kiev'
        self.TIMEZONE_COMMON_NAME = 'Kiev'
        self.bot = telebot.TeleBot(self.__TOKEN)
        self.currencies_rates_text = currencies_rates_text

        @self.bot.message_handler(commands=['start'])
        def _send_welcome(message):
            self.send_welcome(message)

        @self.bot.message_handler(commands=['help'])
        def _help_command(message):
            self.help_command(message)

        @self.bot.message_handler(commands=['list', 'lst'])
        def _get_exchange(message):
            self.get_exchange(message)

        self.bot.infinity_polling()

    @property
    def currencies_rates_text(self):
        print("Getting value")
        return self._currencies_rates_text

    @currencies_rates_text.setter
    def currencies_rates_text(self, text):
        print("Setting value")
        self._currencies_rates_text = text

    def send_welcome(self, message):
        self.bot.send_message(message.chat.id, "Welcome to the club, buddy!")

    def help_command(self, message):
        self.bot.send_message(message.chat.id, 'This is exchange currency bot')

    def get_exchange(self, message):
        self.bot.send_message(message.chat.id, self.currencies_rates_text)

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
