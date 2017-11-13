import requests

with open('token.txt') as soubor:
    token = soubor.read().strip()

headers = {'Authorization': 'token ' + token}

stranka = requests.get('https://api.github.com/user', headers=headers)
stranka.raise_for_status()

print(stranka.text)