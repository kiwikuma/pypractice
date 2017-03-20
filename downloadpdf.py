#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 03:27:33 2017

@author: wf
"""
import shutil

import requests

url = 'http://physikmethoden.weebly.com/uploads/1/1/0/9/11093021/mechanik_bartelmann.pdf'
url2='http://physikmethoden.weebly.com/uploads/1/1/0/9/11093021/mechanik_abraham_marsden.pdf'
response = requests.get(url2, stream=True)
try:    
    with open('img2.pdf', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
except ConnectionResetError as err:
    print(r'connetcion erro', err)
finally:
    print('ok')
del response