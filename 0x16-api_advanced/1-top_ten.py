#!/usr/bin/python3
""""advanced api oth tasks"""
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'Linux/client/0.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return None
    else:
        result = response.json().get('data')
        return result.get('subscribers')
