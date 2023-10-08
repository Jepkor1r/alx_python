"""
Python script that retrieves employees todos list

"""
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
        # Calculate the number of completed and total tasks
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo['completed'])
        # Output the employee's todo list progress
        employee_progresslist = 'Employee {} is done with tasks ({}/{}):'.format(user_data['name'], completed_tasks, total_tasks)
        # Titles of completed tasks
        task_titles = ['\t{}'.format(todo['title']) for todo in todos_data if todo['completed']]
        progress = '\n'.join([employee_progresslist] + task_titles)
        print(progress)
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