# -*- coding: UTF-8 -*-

soubor = open('basnicka.txt', encoding='utf-8')
obsah = soubor.read()
print(obsah)
soubor.close()

# BONUS 1: Zmen program tak aby se na nazev souboru a kodovani zeptal uzivatele z konzole
# BONUS 2: Ptej se uzivatele na jmeno souboru, dokud nezada jmeno, ktere ma priponu .txt
#          Pokud zada neco jineho, pouzorni ho, ze musi pouzit pouze priponu .txt