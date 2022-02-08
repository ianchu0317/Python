# https://assets.breatheco.de/apis/fake/sample/time.php




import requests

if __name__ == '__main__':
	url = 'https://assets.breatheco.de/apis/fake/sample/time.php'

	r = requests.get(url)

	content = r.json()
	print("{0}:{1}:{2}".format(content["hours"], content["minutes"], content["seconds"]))
