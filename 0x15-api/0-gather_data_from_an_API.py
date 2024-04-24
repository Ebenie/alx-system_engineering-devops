#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
from a given employee ID using a REST API.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    api_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        todos = response.json()
        
        user_response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
        user_response.raise_for_status()
        user = user_response.json()

        completed_tasks = [task for task in todos if task.get('completed')]
        total_tasks = len(todos)
        completed_tasks_count = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):".format(user['name'], completed_tasks_count, total_tasks))
        for task in completed_tasks:
            print("\t {}".format(task['title']))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))

