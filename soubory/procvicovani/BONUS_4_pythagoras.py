# -*- coding: UTF-8 -*-
# Napis funkci, ktera ti pro dve zadane delky odvesen pravouhleho 
# trojuhelnika vypocita delku prepony. 
# (TIP budes potrebovat Pythagorovu vetu)

# BONUS: Pridej funkce i pro vypocet strany, 
# pokud zname jednu odvesnu a preponu

# Pythagorova věta: a**2 + b**2 = c**2
from math import sqrt

def vypocti_delku_prepony(odvesna_a, odvesna_b):
    prepona = sqrt(odvesna_a**2 + odvesna_b**2)
    return prepona

def vypocti_delku_strany(odvesna, prepona):
    strana = sqrt(prepona**2 - odvesna**2)
    return strana


