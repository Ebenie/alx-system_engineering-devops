#!/usr/bin/python3

"""
This script retrieves information about employees' TODO lists
using a REST API and exports it to a JSON file.
"""

import requests
import json

if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/todos'
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        todos = response.json()

        todo_dict = {}
        for todo in todos:
            user_id = str(todo['userId'])
            task_info = {
                "username": todo['userId'],
                "task": todo['title'],
                "completed": todo['completed']
            }
            if user_id in todo_dict:
                todo_dict[user_id].append(task_info)
            else:
                todo_dict[user_id] = [task_info]

        json_file = 'todo_all_employees.json'
        with open(json_file, 'w') as file:
            json.dump(todo_dict, file)
        
        print("JSON file '{}' has been created successfully.".format(json_file))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))

