# Send a POST request to the following URL:
# https://assets.breatheco.de/apis/fake/sample/save-project-json.php

# With Content-Type: application/json

'''
With the following request body as JSON text:

{
    "id":2323,
    "title": "Very big project"
}
'''


import requests
import json
import pprint


if __name__ == '__main__':
	url = 'https://assets.breatheco.de/apis/fake/sample/save-project-json.php'
	my_data = {"id":2323, "title": "Very big project"}
	#my_data = json.dumps(my_data)
	r = requests.post(url, json = my_data)

	pprint.pprint(r.json(), sort_dicts=False)
