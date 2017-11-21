#Je potreba naimportovat modul 'json'
import json
jsonRetezecKocka =""" 
{
    "Jméno": "Drobek",
    "OblibenéKrmivo": "CatFood Premium Deluxe",
    "Váha": 11,
    "Rasa": "Pouliční směs"
}
"""

jsonRetezecZEshopu = """
{
    "JménoProduktu": "Kosmodisk",
    "Cena": 2999,
    "Skladem": true
}
"""

nactenyJsonKocicka = json.loads(jsonRetezecKocka)
nactenyJsonKocicka['Odblešena'] = True
print(nactenyJsonKocicka)

