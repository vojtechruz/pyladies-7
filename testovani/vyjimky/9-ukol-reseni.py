class ObsahError(Exception):
    pass

def vypocitej_obsah_ctverce(strana):
    try:
        strana_float = float(strana)

        if strana_float < 0:
            raise ObsahError("Strana nesmi byt zaporne cislo!")

        return strana_float*strana_float
    except ValueError:
        raise ObsahError("Musis zadat desetinne cislo!")

while True:
    zadana_strana = input("Zadej stranu ctverce v centimetrech:")
    try:
        obsah = vypocitej_obsah_ctverce(zadana_strana)
        break
    except ObsahError as error:
        print(error) # Vypise chybovou hlasku z vyjimky
        print("Prosim zadej nezaporne desetinne cislo!")

print("Obsah ctverce je {}".format(obsah))
