# -*- coding: UTF-8 -*-
# Najdi na internetu text své oblíbené písně, zkopíruj si ho do řetězce, a zjisti, kolikrát je v něm použito
# písmeno K

zdroj = input('Zadej zdrojovy text: ')
hledany_retezec = input('Zadej hledany retezec: ')
pocet_vyskytu = zdroj.count(hledany_retezec)

print('Retezec "{0}" se v textu nachazi {1} krat'.format(hledany_retezec, pocet_vyskytu))
