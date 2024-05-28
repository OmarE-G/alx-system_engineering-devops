#!/usr/bin/python3
"""
Gain information from an API
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    id = argv[1]
    data = requests.get(url + f"/todos?userId={id}").json()
    tasks = {}
    tasks[str(id)] = []
    name = requests.get(url + f"/users/{id}").json()['username']
    for task in data:
        task_info = {
            "task": task["title"],
            "username": name,
            "completed": task["completed"]
        }
        tasks[str(id)].append(task_info)

    with open(f'{id}.json', 'w', newline='') as file:
        json.dump(tasks, file)
