#!/usr/bin/python3
""""advanced api oth tasks"""
from unittest import result
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Linux/client/0.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return 0
    else:
        result = response.json().get('data')
        return result.get('subscribers')
