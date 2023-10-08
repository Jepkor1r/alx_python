"""
Python script that retrieves employees todos list

"""

import requests
import sys

def employees_todo_list(ID):
    todos_response = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')
    user_response = requests.get('https://jsonplaceholder.typicode.com/users/1')
    
    if todos_response.status_code == 200 and user_response.status_code == 200:
        todos_data = todos_response.json()
        user_data = user_response.json()
        # Calculate the number of completed and total tasks
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo['completed'])
        # output of the employee's todo list progress
        employee_progresslist = 'Employee {} is done with tasks ({}/{}):'.format(user_data['name'], completed_tasks, total_tasks)
        # titles of completed tasks
        task_tittle =['\t{}'.format(todo['title']) for todo in todos_data if todo['completed']]
        print(employee_progresslist +'\n'.join(task_tittle))      
    else:
        print('HTTPS request failed with status code: {}'.format(todos_response.status_code))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <ID>")
    else:
        try:
            ID = int(sys.argv[1])
            employees_todo_list(ID)
        except ValueError:
            print("Please enter a valid integer for the employee ID.")