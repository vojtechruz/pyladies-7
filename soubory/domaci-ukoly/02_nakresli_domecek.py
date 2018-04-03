# -*- coding: UTF-8 -*-
# Napiš funkci, která vykreslí domeček dané velikosti.
# (t.j. velikost se zadá argumentem)

from turtle import forward, left, right, exitonclick, hideturtle
from math import sqrt

def draw_house(size):
    left(45)
    forward(sqrt(2)*size)
    left(90)
    forward(sqrt(2)*size/2)
    left(90)
    forward(sqrt(2)*size/2)
    left(90)
    forward(sqrt(2)*size)
    right(135)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    # Bez tohoto prikazu bude na konci nakreslene cary sipka
    hideturtle()

house_size = input("Zadej velikost domecku: ")
draw_house(house_size)
exitonclick()
