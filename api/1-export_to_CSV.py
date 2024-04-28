#!/usr/bin/python3
"""
Script Documentation
"""
import csv
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

    csv_writer = csv.writer(open(f"{id}.csv", "w"), quoting=csv.QUOTE_ALL)

    for task in todos:
        csv_writer.writerow(
            [user["id"], user["username"], task["completed"], task["title"]]
        )


if __name__ == "__main__":
    if len(argv) == 2:
        id = int(argv[1])
        main(id)
