#!/usr/bin/python

import json

def get_process_id():
    with open('ihub_parameters.json', "rb") as PFile:
        ihub_data = json.loads(PFile.read().decode('utf-8'))

    return ihub_data['processId']

if __name__ == "__main__":
    print(get_process_id())