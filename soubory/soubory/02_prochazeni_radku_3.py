print('Slyšela jsem tuto básničku:')
print()
soubor = open('basnicka.txt', encoding='utf-8')

for radek in soubor:
    # End urcuje jakym znakem bude zakoncen retezec, ktery se vypisuje
    # Vychozi nastaveni je novy radek, ale muzeme ho nahradit prazdnym retezcem.
    print('    ' + radek, end='')
soubor.close()
print()
print('Jak se ti líbí?')