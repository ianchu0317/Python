import requests

url = input("Enter url to search: ")


r = requests.request('GET', url)

print("Status code is ", r.status_code)
