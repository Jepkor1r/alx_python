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
    
    employee_name = user_data.get("username")

    alltask_record  = []

    for todo_data in todos_data:
        alltask_record.append(
            [
                employee_id,
                employee_name,
                todo_data["completed"],
                todo_data["title"],
            ]
        )

    with open(str(employee_id) + ".csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(alltask_record)


if __name__ == "__main__":
    employees_todo_list(sys.argv[1])