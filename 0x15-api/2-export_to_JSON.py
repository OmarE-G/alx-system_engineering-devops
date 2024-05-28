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
    done = []

    name = requests.get(url + f"/users/{id}").json()['username']
    with open(f'{id}.json', 'w', newline='') as file:
        json.dump(data, file)
