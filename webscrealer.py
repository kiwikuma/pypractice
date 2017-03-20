# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

r = requests.get('https://github.com/timeline.json')
print (r)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
