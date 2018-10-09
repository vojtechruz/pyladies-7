# -*- coding: UTF-8 -*-

with open('druha-basnicka.txt', mode='a', encoding='utf-8') as soubor:
    print('Naše staré hodiny', file=soubor)
    print('Bijí', 2+2, 'hodiny', file=soubor)

# BONUS: rezim zapisu mode='w' prepise cely aktualni obsah souboru, pokud uz existuje.
# Zkus zjistit, zda muzes pouzit jiny rezim, ktery jen prida text na konec existujiciho souboru.
# Podivej se na tuto adresu:
# https://docs.python.org/2/library/functions.html#open