# -*- coding: UTF-8 -*-
# Změň program Kámen, Nůžky, Papír tak, aby opakoval hru dokud uživatel nezadá "konec".

tah_cloveka = ''

while tah_cloveka != 'konec':
    tah_pocitace = 'kamen'
    tah_cloveka = input('kámen, nůžky, nebo papír? ')

    if tah_cloveka == 'kamen':
        if tah_pocitace == 'kamen':
            print('Plichta.')
        elif tah_pocitace == 'nuzky':
            print('Vyhrála jsi!')
        elif tah_pocitace == 'papir':
            print('Počítač vyhrál.')
    elif tah_cloveka == 'nuzky':
        if tah_pocitace == 'kamen':
            print('Počítač vyhrál.')
        elif tah_pocitace == 'nuzky':
            print('Plichta.')
        elif tah_pocitace == 'papir':
            print('Vyhrála jsi!')
    elif tah_cloveka == 'papir':
        if tah_pocitace == 'kamen':
            print('Vyhrála jsi!')
        elif tah_pocitace == 'nuzky':
            print('Počítač vyhrál.')
        elif tah_pocitace == 'papir':
            print('Plichta.')
    elif tah_cloveka == 'konec':
        print('Hra ukoncena uzivatelem.')
    else:
        print('Nerozumím.')
