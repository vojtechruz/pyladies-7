#Je potreba naimportovat modul 'json'
import json

json_retezec_kocka = """ 
{
    "Jméno": "Drobek",
    "OblibenéKrmivo": "CatFood Premium Deluxe",
    "Váha": 11,
    "Rasa": "Pouliční směs"
}
"""

nacteny_json_kocicka = json.loads(json_retezec_kocka)
nacteny_json_kocicka['Odblešena'] = True
print(nacteny_json_kocicka)

