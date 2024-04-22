#!/usr/bin/python3
"""
Script to retrieve and display employee TODO list progress from a REST API and export it to CSV.
"""

import sys
import requests
import csv


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
        user_id = user_data.get('id')
        username = user_data.get('username')

        # Fetch TODO list for the employee
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Prepare data for CSV
        tasks = []
        for task in todo_data:
            task_dict = {
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": task.get('completed'),
                "TASK_TITLE": task.get('title')
            }
            tasks.append(task_dict)

        return tasks

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


def export_to_csv(tasks, user_id):
    """
    Exports tasks data to CSV file.

    Args:
        tasks (list): List of dictionaries containing task information.
        user_id (int): The ID of the employee.

    Returns:
        None
    """
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(tasks)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    tasks = get_employee_todo_progress(employee_id)
    export_to_csv(tasks, employee_id)
