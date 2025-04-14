# -*- coding: UTF-8 -*-
# Zmen program tak, aby se hralo na mrizce o velikosti zadane uzivatelem, 
# ne 20 napevno.

import random
pocet_poli = int(input("Zadej počet herních políček "))

def piskvorky1d():
    herni_pole = "-" * pocet_poli
    na_tahu = "x"

    while True:
        if na_tahu == "x":
            herni_pole = tah_hrace(herni_pole)
            na_tahu = "o"
        elif na_tahu == "o":
            herni_pole = tah_pocitace(herni_pole)
            na_tahu = "x"

        vysledek = vyhodnot(herni_pole)
        print(herni_pole)

        if vysledek != "-":
            if vysledek == "!":
                print("Remiza! {}".format(herni_pole))
            elif vysledek == "x":
                print("Vyhravas nad pocitacem! {}".format(herni_pole))
            elif vysledek == "o":
                print("Bohuzel, pocitac vyhral. {}".format(herni_pole))
            else:
                raise ValueError("Nepripustny vysledek hry '{}'".format(vysledek))
            return

def tah_hrace(herni_pole):
    while True:
        cislo_policka = input("Zadej cislo policka 0-" + str(pocet_poli - 1) + ": ")
        cislo_policka = int(cislo_policka)
        if cislo_policka < 0 or cislo_policka > (pocet_poli - 1):
            print("Prosim zadej cislo v rozmezi 0-" + str(pocet_poli - 1) + ": ")
        elif herni_pole[cislo_policka] != "-":
            print("Policko {} je obsazene, vyber prosim jine.".format(cislo_policka))
        else:
            return tah(herni_pole, cislo_policka, "x")

def tah(herni_pole, cislo_policka, symbol):
    return herni_pole[:cislo_policka] + symbol + herni_pole[cislo_policka + 1:]

def tah_pocitace(herni_pole):

    while True:
        cislo_policka = random.randrange(len(herni_pole))
        if herni_pole[cislo_policka] == "-":
            return tah(herni_pole, cislo_policka, "o")

def vyhodnot(herni_pole):
    if "xxx" in herni_pole:
        return "x"
    elif "ooo" in herni_pole:
        return "o"
    elif "-" not in herni_pole:
        return "!"
    else:
        return "-"

piskvorky1d()
