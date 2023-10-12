"""
Python script to export data in Json format
"""

import json
import requests
import sys

def employees_todo_list(employee_id):
   # Construct the API endpoints based on the provided employee_id
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    # Make API requests
    todos_response = requests.get(todos_url)
    user_response = requests.get(user_url)

    todos_data = todos_response.json()
    user_data = user_response.json()


    employee_name = user_data.get("username")

    # Create a list to store the tasks
    tasks = []

    # Create a dictionary to store the data
    for todo_data in todos_data:
        task = {
            "task": todo_data["title"],
            "completed": todo_data["completed"],
            "username": employee_name
            }
        tasks.append(task)
        
    # Create a dictionary with the employee_id as the key and the list of tasks as the value
    employee_data = {employee_id: tasks}

    # Convert the dictionary to a JSON string
    json_output = json.dumps(employee_data, indent=4)

      # Save the JSON data to a local file
    filename = f"{employee_id}.json" 
    with open(filename, "w") as json_file:
        json.dump(employee_data, json_file, indent=4)

if __name__ == "__main__":
   employee_id = int(sys.argv[1])
   employees_todo_list(employee_id)