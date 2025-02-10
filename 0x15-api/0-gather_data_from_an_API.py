#!/usr/bin/python3
"""
Script to fetch and display an employee's TODO list progress using a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    employee_url = f"{base_url}/users/{employee_id}"
    response = requests.get(employee_url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch employee data for ID {employee_id}")
        return
    employee_data = response.json()
    employee_name = employee_data.get("name")

    # Fetch TODO list for the employee
    todos_url = f"{base_url}/users/{employee_id}/todos"
    response = requests.get(todos_url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for employee ID {employee_id}")
        return
    todos_data = response.json()

    # Calculate completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]

    # Display the progress
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
