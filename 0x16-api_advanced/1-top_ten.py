#!/usr/bin/python3
""""advanced api oth tasks"""
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'Linux/client/0.0'}
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return None
    else:
        result = response.json()['data']['children']
        if not result:
            return None
        values = []
        for i in 10:
            values[i] = result[i]['data'].get('title')
        #   values =   [title for title in result[i] if i < 10]
        # print(result[0]['data'].get('title'))
        print(values)
        return 
