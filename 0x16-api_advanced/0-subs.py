#!/usr/bin/python3
""""advanced api oth tasks"""
import requests
def number_of_subscribers(subreddit):
    headers = {'User-Agent':'Linux/client/0.0'}
    response = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=headers)
    if not response:
        return 0
    else:
        return response
