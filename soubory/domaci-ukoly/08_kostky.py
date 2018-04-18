# -*- coding: UTF-8 -*-
# Napiš program, který simuluje tuto hru:
# První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka. Potom hází další hráč,
# dokud nepadne šestka i jemu. Potom hází hráč třetí, a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky
# potřeboval nejvíc hodů. (V případě shody vyhraje ten, kdo házel dřív.)
# Program by měl vypisovat všechny hody, a nakonec napsat, kdo vyhrál.

import random

def hazej_dokud_nepadne_6():
    pocet_hodu = 0
    while True:
        pocet_hodu = pocet_hodu + 1
        hod = random.randrange(6) + 1
        print("Hrac hodil {}".format(hod))
        if hod == 6:
            print("Hraci se podarilo hodit 6 na pocet hodu: {}".format(pocet_hodu))
            return pocet_hodu

def hraj(pocet_hracu):
    vitezny_hrac = 0
    vitezny_pocet_hodu = 0

    for cislo_hrace in range(1, pocet_hracu+1):
        print("Hraje hrac cislo {}".format(cislo_hrace))
        pocet_hodu = hazej_dokud_nepadne_6()

        if pocet_hodu < vitezny_pocet_hodu or vitezny_pocet_hodu == 0:
            print("Hrac {} je nyni aktualni vitez s poctem hodu {}".format(cislo_hrace, pocet_hodu))
            vitezny_hrac = cislo_hrace
            vitezny_pocet_hodu = pocet_hodu
        else:
            print ("{} neni dost dobry vysledek aby prekonal {}".format(pocet_hodu, vitezny_pocet_hodu))

        print("---------------------------------")

    print ("Vitezi hrac {} s poctem hodu {}".format(vitezny_hrac, vitezny_pocet_hodu))

pocet_hracu = int(input("Zadej pocet hracu "))
hraj(pocet_hracu)
