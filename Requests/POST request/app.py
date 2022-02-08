# Send a POST request to the following URL:
# POST: https://assets.breatheco.de/apis/fake/sample/post.php
# And print the response text on the console

import requests
import pprint

if __name__ == '__main__':
	url = 'https://assets.breatheco.de/apis/fake/sample/post.php'
	my_data = {"testing":"123",
                "name": "Ian"}
	r = requests.post(url, data=my_data)
	pprint.pprint(r.json(), sort_dicts=False)
