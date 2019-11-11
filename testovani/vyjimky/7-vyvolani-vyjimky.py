# Vyjimku lze explicitne vyvolat pomoci prikazu raise

VELIKOST_POLE = 20

def over_cislo(cislo):
    if 0 <= cislo < VELIKOST_POLE:
        print('OK!')
    else:
        raise ValueError('Čislo {n} není v poli!'.format(n=cislo))

over_cislo(52)