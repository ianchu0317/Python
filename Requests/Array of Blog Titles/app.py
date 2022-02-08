# Using the same endpoint from the previous exercise,
# create a function get_titles that returns the titles of all the posts found in the response body.

import requests
import pprint

def get_titles(content):
	posts = content['posts']
	titles = [post['title'] for post in posts]
	return titles


if __name__ == '__main__':

	url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
	r = requests.request('GET', url)
	titles = get_titles(r.json())

	print("Titles are: ")
	pprint.pprint(titles, sort_dicts=False)
