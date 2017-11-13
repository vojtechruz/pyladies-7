import requests

stranka = requests.get('https://api.github.com/user')
stranka.raise_for_status()
print(stranka.text)