# Začínáš s 0 body.
# Počítač v každém kole vypíše, kolik máš bodů, a zeptá se tě, jestli chceš pokračovat.
# Pokud odpovíš „ne“, hra končí.
# Pokud odpovíš „ano“, počítač „otočí kartu“ (náhodně vybere číslo od 2 do 10), vypíše její hodnotu a přičte ji k bodům.
# Pokud máš víc než 21 bodů, prohráváš.
# Cílem hry je získat co nejvíc bodů, ideálně 21.











from random import randrange

soucet = 0
while soucet < 21:
    print('Máš', soucet, 'bodů')
    odpoved = input('Otočit kartu? ')
    if odpoved == 'ano':
        karta = randrange(2, 11)
        print('Otočil/a jsi', karta)
        soucet = soucet + karta
    elif odpoved == 'ne':
        break
    else:
        print('Nerozumím! Odpovídej "ano", nebo "ne"')

if soucet == 21:
    print('Gratuluji! Vyhrál/a jsi!')
elif soucet > 21:
    print('Smůla!', soucet, 'bodů je moc!')
else:
    print('Chybělo jen', 21 - soucet, 'bodů!')