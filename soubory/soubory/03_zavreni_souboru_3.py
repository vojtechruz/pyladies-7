# -*- coding: UTF-8 -*-

def iniciala():
    """Vrátí první písmeno v daném souboru."""

    # Pokud pouziju with, nemusim explicitne zavirat soubor, zavre se sam
    # A to i pokud vyskoci vyjimka
    with open('basnicka.txt', encoding='utf-8') as soubor:
        obsah = soubor.read()
        return obsah[0]

print(iniciala())

# Puvodni kod:
#     soubor = open('basnicka.txt', encoding='utf-8')
#     try:
#         obsah = soubor.read()
#         return obsah[0]
#     finally:
#         soubor.close()