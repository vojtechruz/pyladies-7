# -*- coding: UTF-8 -*-

soubor = open('basnicka.txt', encoding='utf-8')
obsah = soubor.read()
print(obsah)
soubor.close() # Dulezite je soubor vzdy zavrit