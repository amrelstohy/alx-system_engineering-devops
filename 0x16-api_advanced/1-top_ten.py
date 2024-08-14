#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    data = requests.get(url, allow_redirects=False)

    if data.status_code == 200:
        for i in range(10):
            print(data.json()['data']['children'][i]['data']['title'])
    else:
        print("None")
