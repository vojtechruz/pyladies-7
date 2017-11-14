import requests

with open('token.txt') as soubor:
    token = soubor.read().strip()

headers = {'Authorization': 'token ' + token}

# Dokumentace k ulozeni repozitare k oblibenym
# https://developer.github.com/v3/activity/starring/#star-a-repository



stranka = requests.?
stranka.raise_for_status()