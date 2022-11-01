#!/usr/bin/python3
""""advanced api oth tasks"""
import requests


def top_ten(subreddit):
    """"Alx verification of editing tools"""
    headers = {'User-Agent': 'Linux/client/0.0'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        print("None")
        return
    else:
        result = response.json()['data']['children']
        if result is None:
            print("None")
            return
        values = []
        for title in result:
            if len(values) > 10:
                break
            values.append(title['data'].get('title'))
        print(*values, sep='\n')
