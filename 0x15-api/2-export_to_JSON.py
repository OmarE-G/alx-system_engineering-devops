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

    name = requests.get(url + f"/users/{id}").json()['username']
    for task in data:
        tasks[str(id)]['username'] = name
        tasks[str(id)]["task"] = task["title"]
        tasks[str(id)]["completed"] = task["completed"]
        
    with open(f'{id}.json', 'w', newline='') as file:
        json.dump(tasks, file)
