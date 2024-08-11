#!/usr/bin/python3
"""
Python script that, using this REST API.
"""

import csv
import requests
import sys

userid = 2 #sys.argv[1]
x = requests.get('https://jsonplaceholder.typicode.com'
                 f'/users/{userid}').json()
username = x['username']

y = requests.get('https://jsonplaceholder.typicode.com/'
                 f'todos?userId={userid}').json()

with open(f'{userid}.csv', mode='w', ) as file:

    for i in y:
        print(f'{userid},{username},{i['completed']},{i['title']}')
        csv.writer(file).writerow(f'{userid},{username},{i['completed']},{i['title']}')
    file.close()