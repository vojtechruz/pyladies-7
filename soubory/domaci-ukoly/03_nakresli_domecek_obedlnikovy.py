# -*- coding: UTF-8 -*-
# Napiš funkci, která vykreslí domeček dané velikosti.
# (t.j. velikost se zadá argumentem)

from turtle import forward, left, right, exitonclick, hideturtle
from math import sqrt

def nakresli_domecek(vyska, sirka):

    delka_uhlopricky = sqrt(vyska ** 2 + sirka ** 2)

    left(?)
    forward(delka_uhlopricky)
    left(?)
    # Strecha
    forward(delka_uhlopricky / 2)
    left(?)
    # Strecha
    forward(delka_uhlopricky / 2)
    left(?)
    forward(delka_uhlopricky)
    right(?)
    forward(sirka)
    right(?)
    forward(vyska)
    right(?)
    forward(sirka)
    right(?)
    forward(vyska)
    # Bez tohoto prikazu bude na konci nakreslene cary sipka
    hideturtle()

vyska_domecku = input("Zadej vysku domecku: ")
sirka_domecku = input("Zadej sirku domecku: ")
nakresli_domecek(int(vyska_domecku), int(sirka_domecku))
exitonclick()
