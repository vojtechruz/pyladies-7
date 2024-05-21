# Priklad retezce ve formatu JSON
# Trojite uvozovky v Pythonu umoznuji zapsat retezec
# na vice radku
import json

json_retezec = """ 
{
    "jméno": "Drobek",
    "oblibené_krmivo": "CatFood Premium Deluxe",
    "váha": 11,
    "rasa": "Pouliční směs"
}
"""

json_retezec_z_eshopu = """
{
    "jméno_produktu": "Kosmodisk",
    "cena": 2999,
    "skladem": true
}
"""

# Pozor, zapis je mirne jiny nez v Pythonu!