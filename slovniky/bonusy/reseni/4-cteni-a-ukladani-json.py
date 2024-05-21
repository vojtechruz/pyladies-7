#Ukol
# - nacti JSON retezec nize jako Python Slovnik
# - zmen polozku 'Skladem' na False
# - pridej polozku 'Dopravne' s hodnotou 199
# - preved vysledny slovnik na JSON retezec a vypis ho do konzole

import json

json_retezec_z_eshopu = """
{
    "JménoProduktu": "Kosmodisk",
    "Cena": 2999,
    "Skladem": true
}
"""

# Prevedeme json retezec na seznam
seznam = json.loads(json_retezec_z_eshopu)

# Zmena hodnot
seznam["Skladem"] = False
seznam["Dopravne"] = 199

# Znovu prevedeme na retezec
# ensure_ascii=False resi vypisovani specialnich znaku jako diakritika
# indent=2 nastavuje odsazeni proi formatovani
upraveny_json = json.dumps(seznam, ensure_ascii=False, indent=2)
print(upraveny_json)
