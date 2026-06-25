# -*- coding: UTF-8 -*-
# Ptej se uzivatele na cisla, dokud nenapise 'konec'. 
# Potom vypis sumu (soucet) vsech zadanych cisel.

suma = 0
while True:
    zadane_cislo = input("Zadej číslo. Pokud už nechceš pokračovat, napiš 'konec'. ")
    if zadane_cislo.lower() == "konec":
        print("Celkový součet zadaných čísel je:", suma)
        break
    else:
        suma = suma + int(zadane_cislo)