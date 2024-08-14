#!/usr/bin/python3
"""a recursive function that queries the Reddit API."""

import requests


def recurse(subreddit, hot_list=[], file={}):
    if file == {}:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        try:
            data = requests.get(url, allow_redirects=False).json()
            file = data
        except Exception as e:
            return None

    index = len(hot_list)
    if index != len(file['data']['children']):
        hot_list.append(file['data']['children'][index]['data']['title'])
        recurse(subreddit, hot_list, file)

    return hot_list
