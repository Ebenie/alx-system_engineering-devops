#!/usr/bin/python3
"""
1-top_ten
"""
import requests

def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(None)
        return
    
    data = response.json()
    
    if 'data' not in data or 'children' not in data['data']:
        print(None)
        return
    
    posts = data['data']['children']
    
    for post in posts:
        print(post['data']['title'])

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
