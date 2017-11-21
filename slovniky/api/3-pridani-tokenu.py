import requests

#Nacteme token ze souboru token.txt a ulozime do promenne token
with open('token.txt') as soubor:
    token = soubor.read().strip()

#Vytvorime hlavicky s tokenem
headers = {'Authorization': 'token ' + token}

#K volani API je nutne pridat hlavicky obsahujici token
stranka = requests.get('https://api.github.com/user', headers=headers)
stranka.raise_for_status()

print(stranka.text)