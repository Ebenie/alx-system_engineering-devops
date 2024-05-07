#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, after=None, counts={}):
    if after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return
    
    data = response.json()
    
    if 'data' not in data or 'children' not in data['data']:
        return
    
    posts = data['data']['children']
    
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            if word.lower() in title.split():
                counts[word.lower()] = counts.get(word.lower(), 0) + 1
    
    after = data['data']['after']
    
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])

