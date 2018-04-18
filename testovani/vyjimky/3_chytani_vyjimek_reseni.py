def ziskej_Vek_uzivatele():
    while True:
        vekRetezec = input('Zadej prosim svuj vek!\n')

        # Co se stane kdyz uzivatel zada retezec nebo desetinne cislo?
        try:
            vek = int(vekRetezec)
        except ValueError:
            print("{0} neni platne cele cislo!".format(vekRetezec))
            continue

        if vek < 0:
            print("Vek nemuze byt zaporne cislo!")
        elif vek > 120:
            print("To asi zertujes?")
        else:
            print("Vse je v poradku.")
            return vek

vek_uzivatele = ziskej_Vek_uzivatele()
print("Uzivatel zadal vek {0}".format(vek_uzivatele))
