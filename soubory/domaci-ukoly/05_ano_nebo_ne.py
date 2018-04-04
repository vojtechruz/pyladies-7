# -*- coding: UTF-8 -*-
# Změň funkci ano_nebo_ne tak, aby se místo "ano" se dalo použít i "a", místo "ne" i "n", a aby se nebral
# ohled na velikost písmen a mezery před/za odpovědí.

def zeptejSeAnoNe(otazka):
    while True:
        odpoved = input(otazka)
        odpoved = odpoved.strip()
        odpoved = odpoved.upper()

        if odpoved == 'A' or odpoved == 'ANO':
            return True
        elif odpoved == 'N' or odpoved == 'NE':
            return False

        print('Nerozumím...')


stastna = zeptejSeAnoNe('Jsi šťastná? ')
bohata = zeptejSeAnoNe('Jsi bohatá? ')

if bohata and stastna:
    # Je bohatá a zároveň štǎstná, ta se má.
    print('Gratuluji!')
elif bohata:
    # Je bohatá, ale není „bohatá a zároveň šťastná“,
    # takže musí být jen bohatá.
    print('Zkus se víc usmívat.')
elif stastna:
    # Tady musí být jen šťastná.
    print('Zkus míň utrácet.')
else:
    # A tady víme, že není ani šťastná, ani bohatá.
    print('To je mi líto.')
