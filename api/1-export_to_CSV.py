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

        csv_file = os.path.abspath(f"api/{user_data['id']}.csv")

        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)

            # Write the CSV header
            writer.writerow(["User ID", "User Name", "Task Status", "Task Title"])

            # Write each task as a separate row with its status
            for todo in todos_data:
                task_status = "True" if todo['completed'] else "False"
                writer.writerow([user_data["id"], user_data["name"], task_status, todo["title"]])

        print(f"CSV file created at: {csv_file}")
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