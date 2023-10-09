""" 
import csv
import os
import requests
import sys

def employees_todo_list(employee_id):
    # Construct the API endpoints based on the provided employee_id
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    # Make API requests
    todos_response = requests.get(todos_url)
    user_response = requests.get(user_url)
    
    if todos_response.status_code == 200 and user_response.status_code == 200:
        todos_data = todos_response.json()
        user_data = user_response.json()

        # Create the 'api' directory if it doesn't exist
        os.makedirs("api", exist_ok=True)

        csv_file = os.path.abspath(f"api/{user_data['id']}")

        with open(str(csv_file) + ".csv", "w", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)

            # Write the CSV header
            writer.writerow(["User ID", "User Name", "Task Status", "Task Title"])

            # Write each task as a separate row with its status
            for todo in todos_data:
                task_status = "True" if todo['completed'] else "False"
                writer.writerow([user_data["id"], user_data["name"], task_status, todo["title"]])

        print(f"{csv_file}")
    else:
        print('HTTPS request failed with status codes: todos={}, user={}'.format(todos_response.status_code, user_response.status_code))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            employees_todo_list(employee_id)
        except ValueError:
            print("Please enter a valid integer for the employee ID.")
"""

"""
Python script that retrieves employees todos list
Employees data to be exported in the CSV format
"""
import csv
import requests
import sys


def employees_todo_list(employee_id):
    # Construct the API endpoints based on the provided employee_id
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    # Make API requests
    todos_response = requests.get(todos_url)
    user_response = requests.get(user_url)

    todos_data = todos_response.json()
    user_data = user_response.json()

    alltask_record  = []

    for todo_data in todos_data:
        alltask_record.append(
            [
                employee_id,
                user_data,
                todo_data["completed"],
                todo_data["title"],
            ]
        )

    with open(str(employee_id) + ".csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(alltask_record)


if __name__ == "__main__":
    employees_todo_list(sys.argv[1])