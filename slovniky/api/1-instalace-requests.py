#Musis instalovat knihovnu Requests, ktera umoznuje komunikaci pres internet:
#Nezapomen instalaci provest ve virtualnim prostredi!
# python -m pip install requests

import requests

# stažení stránky
stranka = requests.get('https://github.com')

# ověření, že dotaz proběhl v pořádku
stranka.raise_for_status()

# vypsání obsahu
print(stranka.text)

