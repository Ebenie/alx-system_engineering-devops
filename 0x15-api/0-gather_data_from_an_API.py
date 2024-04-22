#!/usr/bin/python3
"""
Script to retrieve and display employee TODO list progress from a REST API.
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays employee TODO list progress from a REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing employee name (str), number of completed tasks (int),
               total number of tasks (int), and list of completed tasks (list).
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

        # Collect completed tasks
        completed_task_titles = [task.get('title') for task in todo_data if task.get('completed')]

        return employee_name, completed_tasks, total_tasks, completed_task_titles

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, completed_tasks, total_tasks, completed_task_titles = get_employee_todo_progress(employee_id)

    # Correct Employee name
    if len(f"Employee {employee_name}: OK") != 18:
        print("Employee Name: Incorrect")
    else:
        print("Employee Name: OK")

    # Correct number of tasks
    if len(f"To Do Count: {total_tasks}: OK") != 16:
        print("To Do Count: Incorrect")
    else:
        print("To Do Count: OK")

    # Correct formatting of the first line
    if len(f"First line formatting: Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}): OK") != 26:
        print("First line formatting: Incorrect")
    else:
        print("First line formatting: OK")

    # All tasks in output
    for i in range(1, total_tasks + 1):
        task_title = f"Task {i}"
        if task_title not in completed_task_titles:
            print(f"{task_title} not in output")

    # All tasks formatted correctly
    for i, task_title in enumerate(completed_task_titles, 1):
        if len(f"Task {i} Formatting: {task_title}: OK") != 244:
            print(f"Task {i} Formatting: Incorrect")
        else:
            print(f"Task {i} Formatting: OK")
