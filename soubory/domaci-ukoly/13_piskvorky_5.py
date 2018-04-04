# -*- coding: UTF-8 -*-
# 1-D piškvorky se hrají na řádku s dvaceti políčky.
# Hráči střídavě přidávají kolečka (o) a křížky (x), třeba:
# 1. kolo: -------x------------
# 2. kolo: -------x--o---------
# 3. kolo: -------xx-o---------
# 4. kolo: -------xxoo---------
# 5. kolo: ------xxxoo---------
# Hráč, která dá tři své symboly vedle sebe, vyhrál.

# Napiš funkci piskvorky1d, která vytvoří řetězec s herním polem, a střídavě volá funkce tah_hrace a
# tah_pocitace, dokud někdo nevyhraje nebo nedojde k remíze.
# Nezapomeň kontrolovat stav hry po každém tahu.

import random

def piskvorky1d():
    herni_pole = "-" * 20
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

# Funkce z minulych ukolu

def tah_hrace(herni_pole):
    while True:
        cislo_policka = input("Zadej cislo policka 0-19: ")
        cislo_policka = int(cislo_policka)
        if cislo_policka < 0 or cislo_policka > 19:
            print("Prosim zadej cislo v rozmezi 0-19.")
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
