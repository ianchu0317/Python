# Using the same endpoint from the previous exercise,
# create a function get_post_tags that returns the array of tags
# of a given post id

import requests
import pprint

def find_ids(content):
	posts = content['posts']
	return [post['id'] for post in posts]

def get_post_tags(id, content):
	posts = content['posts']
	for post in posts:
		if post['id'] == id:
			return post['tags']



if __name__ == '__main__':
	url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
	r = requests.get(url)
	ids = find_ids(r.json())
	print("Availables IDs are: ", ids)

	requested_id = int(input("Enter ID to find tags: "))

	if requested_id not in ids:
		print("ID not found")
		exit()

	tags = get_post_tags(requested_id, r.json())

	print("Tags are: ")
	pprint.pprint(tags, sort_dicts=False)
