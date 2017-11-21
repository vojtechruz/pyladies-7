#Je potreba naimportovat modul 'json'
import json

json_retezec_kocka = """ 
{
    "jméno": "Drobek",
    "oblibené_krmivo": "CatFood Premium Deluxe",
    "váha": 11,
    "rasa": "Pouliční směs"
}
"""

nacteny_json_kocicka = json.loads(json_retezec_kocka)
nacteny_json_kocicka['odblešena'] = True
print(nacteny_json_kocicka)

