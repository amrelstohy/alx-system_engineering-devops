#!/usr/bin/python3
"""
function that queries the Reddit API
and returns the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    this function counts number of sub
    """
    data = requests.get(f'https://www.reddit.com/r/{subreddit}/'
                        'about.json', allow_redirects=False)
    if data.status_code == 200:
        data = data.json()
        return data['data']['subscribers']
    else:
        return 0
