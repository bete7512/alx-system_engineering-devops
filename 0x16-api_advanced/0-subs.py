#!/usr/bin/python3
""""advanced api oth tasks"""
import requests
def number_of_subscribers(subreddit):
    headers = {'User-agent':}
    response = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=headers)
