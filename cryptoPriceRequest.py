from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time, datetime
import os, sys

path = os.path.dirname(os.path.realpath(__file__))

api_key = '8bd66861-c6b1-4c2c-822a-ac59e309d5ac'

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

key_url = 'https://pro-api.coinmarketcap.com/v1/key/info'

map_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}

headers = {
    'Accepts': 'application/json',
    # 'Accept-Encoding': 'deflate, gzip',
    'X-CMC_PRO_API_KEY': api_key
}







def main():

	def json(id):
		delay = (id - 1) * epoch_duration
		time.sleep(delay)
		data = json_request(url, headers, parameters)
		save_json_request(str(data), '') # !!!!!!!!!!!!!!!!!!!!!!!!!!!

	epoch_duration = 2 * 3600
	start_timer()
	whole_day = 24 * 3600
	total_ids = 24 * 3600 // epoch_duration

	while True:
		try:
			th = [Thread(target=json, args=(id,), daemon=True) for id in range(1, 13)]
			for t in th:
				t.start()
			time.sleep(whole_day - 60)
		except:
			pass # !!!!!!!!!!!!!!!!!!!!!
		finally:
			start_timer()