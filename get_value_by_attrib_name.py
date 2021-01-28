#!/usr/bin/python3

import sys
from json import loads

def get_value_by_attrib_name(json):
    ihub_data = loads(json)
    return ihub_data['processId']

print(get_value_by_attrib_name(sys.argv[1]))
