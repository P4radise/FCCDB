#!/usr/bin/python

import sys
import json

def get_process_id(PFile):
    ihub_data = json.loads(PFile)
    return ihub_data['processId']

print(get_process_id(sys.argv[1]))
