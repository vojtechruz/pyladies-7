# Zmen kod tak aby:
# - vypocitej_obsah_ctverce hazela ObsahError kdyz dostane spatnou hodnotu
#      - hodnota musi byt cislo
#      - cislo musi byt nezaporne
# - kdyz se ptas uzivatele na vstup zjisti, jestli nastal ObsahError a kdyz ano, ptej se znovu

class ObsahError(Exception):
    pass

def vypocitej_obsah_ctverce(strana):
    strana_float = float(strana)
    return strana_float*strana_float

zadana_strana = input("Zadej stranu ctverce v centimetrech:")
obsah = vypocitej_obsah_ctverce(zadana_strana)
print("Obsah ctverce je {}".format(obsah))

