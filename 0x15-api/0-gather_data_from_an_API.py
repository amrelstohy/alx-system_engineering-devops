#!/usr/bin/python3
"""
Python script that, using this REST API.
"""

if __name__ == "__main__":
    import requests
    import sys

    count = 0
    task = ""
    id = sys.argv[1]
    n = requests.get('https://jsonplaceholder.typicode.com'
                     f'/users/{id}').json()
    n = n.get("name")
    x = requests.get('https://jsonplaceholder.typicode.com/'
                     f'todos?userId={id}')
    tasks = x.json()
    for i in tasks:
        if i['completed'] is True:
            count += 1
            task += '     ' + i['title'] + '\n'

    print(f"Employee {n} is done with tasks({count}/{len(tasks)}):" + 
          task, end=(''))
