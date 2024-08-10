#!/usr/bin/python3
"""
Python script that, using this REST API.
"""

import requests
import sys


count = 0
task = ""
id = sys.argv[1]
name = requests.get('https://jsonplaceholder.typicode.com'
                    f'/users?id={id}').json()

name = name[0]["name"]
x = requests.get('https://jsonplaceholder.typicode.com/'
                 f'todos?userId={id}')
tasks = x.json()
for i in tasks:
    if i['completed'] is True:
        count += 1
        task += i['title'] + '\n'

print(f"Employee {name} is done with tasks({count}/{len(tasks)}):\n"
      + task, end=(''))
