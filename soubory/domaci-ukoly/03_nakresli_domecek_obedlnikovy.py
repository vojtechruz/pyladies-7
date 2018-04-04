# -*- coding: UTF-8 -*-
# Napiš funkci, která vykreslí domeček dané velikosti.
# (t.j. velikost se zadá argumentem)

from turtle import forward, left, right, exitonclick, hideturtle
from math import sqrt, asin, degrees

def nakresli_domecek(vyska, sirka):

    delka_uhlopricky = sqrt(vyska ** 2 + sirka ** 2)
    uhel = degrees(asin(vyska / delka_uhlopricky))

    left(uhel)
    forward(delka_uhlopricky)
    left(180 - 2 * uhel)
    # Strecha
    forward(delka_uhlopricky / 2)
    left(uhel * 2)
    # Strecha
    forward(delka_uhlopricky / 2)
    left(180 - 2 * uhel)
    forward(delka_uhlopricky)
    right(180 - uhel)
    forward(sirka)
    right(90)
    forward(vyska)
    right(90)
    forward(sirka)
    right(90)
    forward(vyska)
    # Bez tohoto prikazu bude na konci nakreslene cary sipka
    hideturtle()

vyska_domecku = input("Zadej vysku domecku: ")
sirka_domecku = input("Zadej sirku domecku: ")
nakresli_domecek(int(vyska_domecku), int(sirka_domecku))
exitonclick()
