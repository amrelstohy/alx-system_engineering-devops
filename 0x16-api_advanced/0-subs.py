#!/usr/bin/python3
"""
function that queries the Reddit API
and returns the number of subscribers.
"""

import json
import requests


def number_of_subscribers(subreddit):
    try:
        data = requests.get(f'https://www.reddit.com/r/{subreddit}/'
                            'about.json').content
        data = json.loads(data)
        return data['data']['subscribers']
    except Exception:
        return 0