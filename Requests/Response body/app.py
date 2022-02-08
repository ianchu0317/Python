# Print on the console the response body only for 200 requests, 
# for all the other print "Something went wrong".
# https://assets.breatheco.de/apis/fake/sample/random-status.php

import requests

if __name__ == '__main__':
	url = 'https://assets.breatheco.de/apis/fake/sample/random-status.php'

	r = requests.request('GET', url)

	if r.ok:
		print("Content is: {0} [{1}]".format(r.text, r.status_code))
	else:
		print("Content is: {0} [{1}]".format(r.text, r.status_code))
