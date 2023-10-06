import requests

todos_response = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')
user_response = requests.get('https://jsonplaceholder.typicode.com/users/1')

if todos_response.status_code == 200 and user_response == 200:
    todos_data = todos_response.json()
    user_data = user_response.json()
 # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Print the employee's progress
    print('Employee {} is done with tasks ({}/{}):\n'.format(user_data['name'], completed_tasks, total_tasks))

    # Print the titles of completed tasks
    for todo in todos_data:
        if todo['completed']:
            print('\t{}'.format(todo['title']))
else:
    print('HTTPS request failed with status code: {}'.format(todos_response.status_code))