#!/usr/bin/python3
"""
Script to retrieve and display employee TODO list progress from a REST API and export it to JSON.
"""

import sys
import requests
import json


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays employee TODO list progress from a REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: List of dictionaries containing task information.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch employee data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        username = user_data.get('username')

        # Fetch TODO list for the employee
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Prepare data for JSON
        tasks = []
        for task in todo_data:
            task_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
            tasks.append(task_dict)

        return tasks

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


def export_to_json(tasks, user_id):
    """
    Exports tasks data to JSON file.

    Args:
        tasks (list): List of dictionaries containing task information.
        user_id (int): The ID of the employee.

    Returns:
        None
    """
    filename = f"{user_id}.json"
    with open(filename, mode='w') as file:
        json.dump({user_id: tasks}, file, indent=4)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    tasks = get_employee_todo_progress(employee_id)
    export_to_json(tasks, employee_id)
