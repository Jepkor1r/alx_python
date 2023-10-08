"""
Python script that retrieves employees todos list
Employees data to be exported in the CSV format
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

        csv_file = f"api/{user_data['id']}.csv"
            
        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            # Write the CSV header
            writer.writerows(["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"])

            for todo in todos_data:
                # Extract task details
                user_id = user_data['id']
                username = user_data['name']
                task_completed = todo['completed']
                task_title = todo['title']
                
                # Write task as a CSV row
                writer.writerow([user_id, username, str(task_completed), task_title])
        
        print("{csv_file}")
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


