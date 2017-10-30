# -*- coding: UTF-8 -*-

from piskvorky import tah, tah_hrace, tah_pocitace, vyhodnot

# 1-D piškvorky se hrají na řádku s dvaceti políčky.
# Hráči střídavě přidávají kolečka (o) a křížky (x), třeba:
# 1. kolo: -------x------------
# 2. kolo: -------x--o---------
# 3. kolo: -------xx-o---------
# 4. kolo: -------xxoo---------
# 5. kolo: ------xxxoo---------
# Hráč, která dá tři své symboly vedle sebe, vyhrál.

#Nejdrive se vytvori herni plan, pote se strida tah hrace a pociace, dokud nekdo nevyhraje.

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
        break