#!/usr/bin/python3
"""
Script Documentation
"""
import json
import requests
from sys import argv


def main():
    """
    Method Documentation
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/".format(base_url)

    users = requests.get(user_url).json()

    final_dict = {}

    for user in users:
        todos = requests.get(
            "{}/todos?userId={}".format(base_url, user.get("id"))
        ).json()
        new_user_list = []

        for todo in todos:
            new_user_list.append(
                {
                    "username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                }
            )

            final_dict[user.get("id")] = new_user_list

    with open("todo_all_employees.json", "w") as f:
        json.dump(final_dict, f)


if __name__ == "__main__":
    main()
