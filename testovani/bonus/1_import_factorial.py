#Ukol: Z modulu math importuj funkci factorial
#Zeptej se uzivatele na cislo, a vypocuitej faktorial tohoto cisla.
#Vice o funkcich z math: https://docs.python.org/2/library/math.html

#Rozsirujici zadani:
# - Osetri vstup tak, aby uzivatel mohl zadat pouze cele cislo
# - Osetri vstup tak aby uzivatel nemohl zadat zaporne cislo

from math import factorial

while True:
    odpoved = input('Zadej celé kladné číslo ')
    try:
        cislo = int(odpoved)
    except ValueError:
        print('Toto není celé číslo! Zkus to znovu.')
    else:
        if int(odpoved) < 0:
            print('Toto není kladné číslo! Zkus to znovu.')
        else:
            break

faktorial_cisla = factorial(cislo)
print('Faktorial čísla {0} je {1}.'.format(cislo, faktorial_cisla))

