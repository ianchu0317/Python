# The following endpoint returns a JSON formated response with several projects in a list:

# GET: https://assets.breatheco.de/apis/fake/sample/project_list.php

import requests
import pprint
url = 'https://assets.breatheco.de/apis/fake/sample/project_list.php'
r = requests.get(url)
d = r.json()

second_project = d[1]
pprint.pprint(second_project, sort_dicts = False)
print("Second project name: ", second_project["name"])
# print(d)
