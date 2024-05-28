#!/usr/bin/python3
"""
Gain information from an API
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    id = argv[1]
    data = requests.get(url + f"/todos?userId={id}").json()
    done = []

    name = requests.get(url + f"/users/{id}").json()['name']
    with open(f'{id}.csv', 'w') as file:
        for task in data:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow([id, name, task['completed'], task['title']])
