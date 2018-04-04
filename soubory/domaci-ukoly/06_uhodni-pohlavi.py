# -*- coding: UTF-8 -*-
# Napiš program, který se zeptá na příjmení uživatelky/uživatele, a zkusí podle něj uhodnout její/jeho
# pohlaví.

prijmeni = ''
while prijmeni == '':
    prijmeni = input('Zadej svoje prijmeni. ')

    if prijmeni.endswith('á') or prijmeni.endswith('ova'):
        print('Jsi zena')
    elif prijmeni != '':
        print('Jsi muz.')    
