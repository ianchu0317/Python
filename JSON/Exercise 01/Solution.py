#!/usr/bin/env python3
import json

my_json = '{ "Name":"David", "Class":"I", "Age":6 }'
data = json.loads(my_json)
print("{0} -> {1}".format(my_json, type(my_json)))
print("{0} -> {1}".format(data, type(data)))

