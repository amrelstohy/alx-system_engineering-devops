#!/usr/bin/python3
"""
Python script that, using this REST API.
"""

if __name__ == '__main__':
    import csv
    import requests
    import sys

    userid = sys.argv[1]
    x = requests.get('https://jsonplaceholder.typicode.com'
                     f'/users/{userid}').json()
    username = x['username']

    y = requests.get('https://jsonplaceholder.typicode.com/'
                     f'todos?userId={userid}').json()

    with open(f'{userid}.csv', mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in y:
            writer.writerow([userid, username, i['completed'], i['title']])
        file.close()
