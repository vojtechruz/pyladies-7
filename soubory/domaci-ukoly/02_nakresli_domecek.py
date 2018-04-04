# -*- coding: UTF-8 -*-
# Napiš funkci, která vykreslí domeček dané velikosti.
# (t.j. velikost se zadá argumentem)

from turtle import forward, left, right, exitonclick, hideturtle
from math import sqrt

def nakresli_domecek(delka_strany):

    delka_uhlopricky = sqrt(2 * delka_strany ** 2)

    left(45)
    forward(delka_uhlopricky)
    left(90)
    # Strecha
    forward(delka_uhlopricky / 2)
    left(90)
    # Strecha
    forward(delka_uhlopricky / 2)
    left(90)
    forward(delka_uhlopricky)
    right(135)
    forward(delka_strany)
    right(90)
    forward(delka_strany)
    right(90)
    forward(delka_strany)
    right(90)
    forward(delka_strany)
    # Bez tohoto prikazu bude na konci nakreslene cary sipka
    hideturtle()

velikost_domecku = input("Zadej velikost domecku: ")
nakresli_domecek(int(velikost_domecku))
exitonclick()
