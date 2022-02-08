# GET https://assets.breatheco.de/apis/fake/sample/project1.php

import requests

url = 'https://assets.breatheco.de/apis/fake/sample/project1.php'
r = requests.get(url).json()
print("Project name: ", r.get('name'))
