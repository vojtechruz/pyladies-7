#Ukol - pridej podminku, ze pokud uzivatel nezada cislo (ale napr. retezec),
#tak mu program napise, ze pro obvod je potreba cislo a bude se ptat dal,
#dokud opravdu nedostane cislo.

while True:
    strana = float(input('Zadej stranu ctverce v centimetrech: '))
    if strana <= 0:
        print('Delka strany musi byt kladne cislo!')
    else:
        break

print("Obsah ctverce je {}".format(strana*strana))
