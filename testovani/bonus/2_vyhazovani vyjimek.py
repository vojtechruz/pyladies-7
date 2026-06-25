#Ukol: At uzivatel zada desetinne cislo v rozmezi 50.0 a 150.0
# - pokud neni zadano desetinne cislo, ptej se stale znovu
# - pokud cislo je desetinne, ale neni v tomto rozmezi 
#   vyhod ValueError vyjimku

while True:
    odpoved = input('Zadej desetinné číslo v rozmezí 50.0 a 150.0 ')
    if '.' not in odpoved:
        print('Toto není desetinné číslo! Zkus to znovu.')
    else:
        break

if float(odpoved) < 50.0 or float(odpoved) > 150.0:
    raise ValueError('Číslo není v daném rozmezí! ')

