import requests
from pprint import pprint

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(
    url
)

users = response.json()

pprint(users)

flag = True