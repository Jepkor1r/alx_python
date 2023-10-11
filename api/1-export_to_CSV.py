"""
Python script that retrieves employees todos list
Employees data to be exported in the CSV format
"""
#!/usr/bin/python3
import csv
import requests
import sys


def employees_todo_list(employee_id):
  
    todos_data = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)).json()
    employee_name = requests.get("https://jsonplaceholder.typicode.com/users?={}".format(employee_id)).json()[0]["username"]

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