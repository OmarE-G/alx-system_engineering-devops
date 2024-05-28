#!/usr/bin/python3
"""
Gain information from an API
"""
import json
import requests
from sys import argv

if __name__ == '__main__':

    def get_uname(id, users):
        ''' return username using id'''
        return users[id - 1]['username']

    url = 'https://jsonplaceholder.typicode.com/'
    data = requests.get(url + "/todos").json()
    users = requests.get(url + "/users").json()
    tasks = {}
    for task in data:
        i += 1
        id = task["userId"]
        if not tasks.get(str(id)):
            tasks[str(id)] = []
        task_info = {
            "username": get_uname(id, users),
            "task": task["title"],
            "completed": task["completed"]
        }
        tasks[str(id)].append(task_info)

    with open('todo_all_employees.json', 'w', newline='') as file:
        json.dump(tasks, file)
