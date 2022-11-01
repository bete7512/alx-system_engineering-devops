#!/usr/bin/python3
""""advanced api oth tasks"""
import requests


def recurse(subreddit, hot_list=[]):
    """"Alx verification of editing tools"""
    headers = {'User-Agent': 'Linux/client/0.0'}
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return None
    result = response.json()['data']['children']
    max_count = len(result)
    count = len(hot_list)
    if hot_list == []:
        count = 0
    if count < max_count:
        hot_list.append(result[count])
        recurse(subreddit,hot_list)
    return hot_list

    