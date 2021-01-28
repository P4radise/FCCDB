#!/usr/bin/python3

import json

def get_process_id():
    with open("ihub_parameters.json", "rb") as PFile:
        ihub_data = json.loads(PFile.read().decode('utf-8'))

    return ihub_data['processId']

print(get_process_id())
