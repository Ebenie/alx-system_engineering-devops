#!/usr/bin/python3
"""
Script to retrieve and display employee TODO list progress from a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays employee TODO list progress from a REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch employee data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Fetch TODO list for the employee
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Calculate progress
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task.get('completed'))

        # Display progress
        print(f"Employee {employee_name} is done with tasks "
              f"({completed_tasks}/{total_tasks}):")

        # Display completed tasks
        for task in todo_data:
            if task.get('completed'):
                print(f"\t{task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
