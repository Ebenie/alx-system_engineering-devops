#!/usr/bin/python3
"""
Script to retrieve and display all employee TODO list progress from a REST API and export it to JSON.
"""

import sys
import requests
import json


def get_all_employees_todo_progress():
    """
    Retrieves and displays all employee TODO list progress from a REST API.

    Returns:
        dict: Dictionary containing tasks information for all employees.
    """
    base_url = 'https://jsonplaceholder.typicode.com/users'
    try:
        # Fetch all employees data
        employees_response = requests.get(base_url)
        employees_data = employees_response.json()
        
        all_tasks = {}

        for employee in employees_data:
            employee_id = employee.get('id')
            username = employee.get('username')
            
            user_todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
            todo_response = requests.get(user_todo_url)
            todo_data = todo_response.json()
            
            tasks = []
            for task in todo_data:
                task_dict = {
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                tasks.append(task_dict)
            
            all_tasks[employee_id] = tasks

        return all_tasks

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


def export_to_json(all_tasks):
    """
    Exports tasks data for all employees to JSON file.

    Args:
        all_tasks (dict): Dictionary containing tasks information for all employees.

    Returns:
        None
    """
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as file:
        json.dump(all_tasks, file, indent=4)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    all_tasks = get_all_employees_todo_progress()
    export_to_json(all_tasks)
