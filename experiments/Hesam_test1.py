import requests

response = requests.get('https://randomuser.me/api/?results=10')
print(type(response))
data = response.json()

for user in data['results']:
    print(user['name']['first'])


