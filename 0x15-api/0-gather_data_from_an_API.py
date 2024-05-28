#!/usr/bin/python3
"""
Gain information from an API
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    id = argv[1]
    data = requests.get(url + f"/todos?userId={id}").json()
    done = []

    for task in data:
        if task['completed'] is True:
            done.append(task)

    name = requests.get(url + f"/users/{id}").json()['name']
    print(f"Employee {name} is done with tasks({len(done)}/{len(data)}):")
    for task in done:
        print(f"\t {task['title']}")
