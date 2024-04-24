#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
from a given employee ID using a REST API and exports it to a CSV file.
"""

import sys
import requests
import csv

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

        csv_file = '{}.csv'.format(employee_id)
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in todos:
                writer.writerow([user['id'], user['username'], task['completed'], task['title']])
        
        print("CSV file '{}' has been created successfully.".format(csv_file))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))

