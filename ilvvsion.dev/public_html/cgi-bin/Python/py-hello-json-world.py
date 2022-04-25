#!/usr/bin/python3
import json
print ("Cache-control: no-cache")
print ("Content-type: application/json\n\n")

data = {
    'title': 'Hello, Python!',
    'h1': 'Hello, Python!',
    'p': 'Hello World from Python!',
    'time': 'Todays date is  datetime.datetime(2022, 4, 22, 2, 49, 52, 642270)',
    'address': 'Your IP Address: 71.142.246.231'
}

json_string = json.dumps(data)
print(json_string)
