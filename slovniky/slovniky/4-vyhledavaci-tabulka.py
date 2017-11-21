#Seznam hodnot stejneho typu, ve kterych se vyhledava podle klice
#Napr:
    #Telefonni cisla dle jmena
    #Cena dle jmena vyrobku
    #...
zlate_stranky = {
    'alice': '603888921',
    'bohous':'777891776',
    'cyril':'602345666',
    'daniela':'728910000',
    'eva':'777633798',
    'filip':'608915433',
}

#Jak zjistim jake cislo ma Eva?
print('Eva ma cislo {}'.format(zlate_stranky['eva']))