#!/usr/bin/python3
"""
Script Documentation
"""
import requests
from sys import argv


def main(id):
    """
    Method Documentation
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, id)
    todo_url = "{}/todos?userId={}".format(base_url, id)

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    user_name = user.get("name")
    total_tasks = len(todos)
    completed_tasks = [
        task.get("title") for task in todos if task.get("completed")
    ]
    completed_tasks_count = len(completed_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_name, completed_tasks_count, total_tasks
        )
    )

    for task in completed_tasks:
        print("\t " + task)


if __name__ == "__main__":
    if len(argv) == 2:
        id = int(argv[1])
        main(id)