#Ukol

while True:
    strana = float(input('Zadej stranu čtverce v centimetrech: '))
    if strana <= 0:
        print('Delka strany musi byt kladne cislo!')
    else:
        break;

print("Obvod ctverce je {}".format(strana*strana))
