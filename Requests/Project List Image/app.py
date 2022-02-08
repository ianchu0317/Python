# Do a GET request to the same URL as in the previous exercise,
# print the last image URL in the last project.
# https://assets.breatheco.de/apis/fake/sample/project_list.php

import requests

url = 'https://assets.breatheco.de/apis/fake/sample/project_list.php'
r = requests.request('GET', url)
d = r.json()
last_project = d[-1]
last_image_url = last_project.get("images")[-1]

print(last_image_url)

