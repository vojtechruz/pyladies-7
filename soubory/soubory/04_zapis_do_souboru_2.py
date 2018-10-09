# -*- coding: UTF-8 -*-

# Misto puvodniho zpusobu pomoci 'soubor.write' lze pouzit alternativu pomoci 'print'
with open('druha-basnicka.txt', mode='w', encoding='utf-8') as soubor:
    print('Naše staré hodiny', file=soubor)
    print('Bijí', 2+2, 'hodiny', file=soubor)

# Puvodni zpusob pomoci 'soubor.write'
# with open('druha-basnicka.txt', mode='w', encoding='utf-8') as soubor:
#     soubor.write('Naše staré hodiny\n')
#     soubor.write('Bijí čtyři hodiny\n')