#!/usr/bin/python3
""""advanced api oth tasks"""
import requests


def recurse(subreddit, hot_list=[]):
    """"Alx verification of editing tools"""
    headers = {'User-Agent': 'Linux/client/0.0'}
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    count = 0
    data_list = response['data']['children'][count]

    