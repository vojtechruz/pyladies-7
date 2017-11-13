#Slovniky - Sklada se z dvojic klic-hodnota
    #Napr. Vek -> 30
    #Jmeno -> 'Jana'
    #OblibenaBarva - > 'Modra'

osoba = {
    'Jmeno': 'Jana',
    'Vek': 30,
    'OblibenaBarva': 'Modra'
}

print(osoba)

#K polozkam se nepristupuje pres ciselny index, ale klic
print('Jmeno osoby je {}'.format(osoba['Jmeno']))
print('Vek osoby je {}'.format(osoba['Vek']))
print('Oblibena barva osoby je {}'.format(osoba['OblibenaBarva']))

#Kdyz pristoupime k neexistujicimu klici, nastane chyba KeyError
print('Barva oci osoby je {}'.format(osoba['BarvaOci']))

#Nove polozky lze pridavat
osoba['BarvaOci'] = 'Zelena'

#Polozky lze i odebirat
del osoba['Vek']
print(osoba)