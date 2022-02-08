import json

python_obj = {
  "name": "David",
  "class":"I",
  "age": 6
}

json_obj = json.dumps(python_obj)

print("{0} -> {1}".format(python_obj, type(python_obj)))
print("{0} -> {1}".format(json_obj, type(json_obj)))
