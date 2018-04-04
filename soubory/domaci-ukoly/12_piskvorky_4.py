# -*- coding: UTF-8 -*-
# 1-D piškvorky se hrají na řádku s dvaceti políčky.
# Hráči střídavě přidávají kolečka (o) a křížky (x), třeba:
# 1. kolo: -------x------------
# 2. kolo: -------x--o---------
# 3. kolo: -------xx-o---------
# 4. kolo: -------xxoo---------
# 5. kolo: ------xxxoo---------
# Hráč, která dá tři své symboly vedle sebe, vyhrál.

# Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici, na kterou hrát, a vrátí
# herní pole se zaznamenaným tahem počítače.
# Použij jednoduchou náhodnou „strategii”:
# 1. Vyber číslo od 0 do 19
# 2. Pokud je dané políčko volné, hrej na něj
# 3. Pokud ne, opakuj od bodu 1
# Hlavička funkce by tedy měla vypadat nějak takhle:
# def tah_pocitace(pole):
# "Vrátí herní pole se zaznamenaným tahem počítače"
# ...

import random

def tah_pocitace(herni_pole):

    while True:
        cislo_policka = random.randrange(len(herni_pole))
        if herni_pole[cislo_policka] == "-":
            return tah(herni_pole, cislo_policka, "o")


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
