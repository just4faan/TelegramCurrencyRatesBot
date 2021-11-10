import json

import requests
import datetime
from datetime import datetime, timedelta


class WebService:
    def __init__(self):
        self.BASE_URL = 'https://freecurrencyapi.net/api/v2/'
        self.__API_KEY = 'YOUR_API'
        self.__API_KEY = '87e07f20-3508-11ec-9594-63b97110f843'
        self.LATEST_ENDPOINT = 'latest?'
        self.HISTORICAL_ENDPOINT = 'historical?'

    def get_historical_json_currencies(self):
        today = datetime.today().strftime('%Y-%m-%d')

        # Today date object minus 7 days
        today_delta = datetime.today() - timedelta(days=7)
        seven_days_before_today = today_delta.strftime('%Y-%m-%d')

        headers_historical_rates = {'apikey': self.__API_KEY,
                                    'date_from': seven_days_before_today,
                                    'date_to': today}

        historical_url = self.BASE_URL + self.HISTORICAL_ENDPOINT
        print(historical_url)
        response = requests.request("GET", historical_url, headers=headers_historical_rates)
        historical_response = response.json()

        return historical_response

    def get_latest_json_currencies(self):
        headers_latest_rates = {'apikey': self.__API_KEY}
        latest_url = self.BASE_URL + self.LATEST_ENDPOINT
        print(latest_url)
        response = requests.request("GET", latest_url, headers=headers_latest_rates)
        latest_response = response.json()

        return latest_response


if __name__ == '__main__':
    webb = WebService()
    print(webb.get_historical_json_currencies())
    print(webb.get_latest_json_currencies())
    print(webb.get_latest_json_currencies().keys())
