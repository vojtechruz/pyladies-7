# -*- coding: UTF-8 -*-

print('Slyšela jsem tuto básničku:')
print()
soubor = open('basnicka.txt', encoding='utf-8')

for radek in soubor:
    print('    ' + radek)

soubor.close()
print()
print('Jak se ti líbí?')

# Kazdy radek je nasledovan prazdnym radkem. Jak to opravime?