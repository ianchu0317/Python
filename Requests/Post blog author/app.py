# Take a moment to understand the response body when doing a GET request to this endpoint: 
# https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php

import requests
import pprint

url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
r = requests.request('GET', url)
d = r.json()
first_post = d['posts'][0] # Index of first post
author_of_first_post = first_post['author']
author_name = author_of_first_post['name']

# pprint.pprint(d, sort_dicts=False)
print("Author is :", author_name)

