__author__ = 'tayyi'

import requests
import json

payload = {'ajax': '1', 'geo': 'SG', 'date': '2013'}
r = requests.post("http://www.google.com/trends/topcharts/category", payload)
data = r.json()
print(data['entityList'])


