# -*- coding: UTF-8 -*-

print('Slyšela jsem tuto básničku:')
print()
soubor = open('basnicka.txt', encoding='utf-8')

for radek in soubor:
    # rstrip() ostrani bile znaky na konci retezce
    print('    '+radek.rstrip())

soubor.close()
print()
print('Jak se ti líbí?')
