#!/usr/bin/python3
"""
Script to fetch an employee's TODO list and export it to a CSV file.
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches an employee's TODO list and exports it to a CSV file.

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
    employee_name = employee_data.get("username")

    # Fetch TODO list for the employee
    todos_url = f"{base_url}/users/{employee_id}/todos"
    response = requests.get(todos_url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for employee ID {employee_id}")
        return
    todos_data = response.json()

    # Prepare data for CSV
    csv_data = []
    for task in todos_data:
        csv_data.append([
            employee_id,
            employee_name,
            str(task.get("completed")),
            task.get("title")
        ])

    # Write data to CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(csv_data)

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
