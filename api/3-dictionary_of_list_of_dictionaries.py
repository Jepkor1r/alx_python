"""
Python script to export data in Json format
"""

import json
import requests
import sys

def employees_todo_list():
    # Initialize an empty list to store data for all employees
    all_employees_data = []

    for employee_id in range(1, 11):  # Assuming there are employees with IDs from 1 to 10
        # Construct the API endpoints based on the employee_id
        todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

        # Make API requests
        todos_response = requests.get(todos_url)
        user_response = requests.get(user_url)

        todos_data = todos_response.json()
        user_data = user_response.json()

        employee_name = user_data.get("username")

        # Create a list to store the tasks for the current employee
        tasks = []

        for todo_data in todos_data:
            task = {
                "task": todo_data["title"],
                "completed": todo_data["completed"],
                "username": employee_name
            }
            tasks.append(task)

        # Create a dictionary with the employee_id as the key and the list of tasks as the value
        employee_data = {employee_id: tasks}

        # Append the employee_data to the list of all employees
        all_employees_data.append(employee_data)

    # Save the JSON data for all employees to a local file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_data, json_file, indent=4)

if __name__ == "__main":
    employees_todo_list()