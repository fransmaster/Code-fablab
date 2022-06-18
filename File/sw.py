import requests
data=requests.get('https://swapi.dev/api/people/4')
x = data.json()
print(x['name'])
