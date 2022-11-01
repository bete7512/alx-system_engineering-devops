#!/usr/bin/python3
""""advanced api oth tasks"""
import requests


def recurse(subreddit, hot_list=[]):
    """"Alx verification of editing tools"""
    headers = {'User-Agent': 'Linux/client/0.0'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    response = requests.get(url, headers=headers,allow_redirects=False)
    if response.status_code == 404:
        return None
    result = response.json()['data']['children']
    max_count = len(result)
    count = len(hot_list)
    if len(hot_list) >= max_count:
        return
    if hot_list == []:
        count = 0
    # else:
    #     count = count +1
    print(count)
    if count < max_count:
        hot_list.append(result[count])
        recurse(subreddit,hot_list)
    return hot_list

    