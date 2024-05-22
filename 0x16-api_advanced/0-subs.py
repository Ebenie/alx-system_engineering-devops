#!/usr/bin/python3
"""
This module contains a function to fetch the number of subscribers for a specified subreddit from Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the total number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(api_url, headers=user_agent, allow_redirects=False)
    
    if response.status_code == 200:
        subreddit_data = response.json()
        return subreddit_data['data'].get('subscribers', 0)
    return 0

