#!/usr/bin/python3
"""
Script Documentation
"""
import json
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

    final_dict = {
        f"{id}": []
    }

    for task in todos:
        final_dict[f"{id}"].append(
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user["username"],
            }
        )

    with open(f"{id}.json", "w") as f:
        json.dump(final_dict, f)


if __name__ == "__main__":
    if len(argv) == 2:
        id = int(argv[1])
        main(id)
