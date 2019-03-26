from math import pi

def obsah_okruhu(polomer):
    "Vypocita obsah kruhu pro dany polomer"
    return pi * polomer ** 2


def objem_valce(polomer_podstavy, vyska):
    "Vypocita objem valce pro dany polomer podstavy a vysku"
    return obsah_okruhu(polomer_podstavy) * vyska


print(objem_valce(2, 10))
