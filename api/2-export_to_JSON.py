"""
Python script to export data in Json format
"""

import json
import requests

def get_all_employees_info():
    # Get all employees
    employees_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(employees_url)
    employees = response.json()

    # Prepare data for JSON
    all_employee_data = {}
    for employee in employees:
        user_id = employee['id']
        username = employee['username']

        # Get employee's TODO list
        todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        response = requests.get(todos_url)
        todos = response.json()

        # Prepare TODO data for the current employee
        employee_todos = []
        for todo in todos:
            task_data = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            employee_todos.append(task_data)

        # Add TODO data to the dictionary
        all_employee_data[user_id] = employee_todos

    # Write data to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_employee_data, jsonfile, indent=4)
