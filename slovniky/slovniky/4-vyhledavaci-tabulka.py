#Seznam hodnot stejneho typu, ve kterych se vyhledava podle klice
#Napr:
    #Telefonni cisla dle jmena
    #Cena dle jmena vyrobku
    #...
zlateStranky = {
    'Alice': '603888921',
    'Bohous':'777891776',
    'Cyril':'602345666',
    'Daniela':'728910000',
    'Eva':'777633798',
    'Filip':'608915433',
}

#Jak zjistim jake cislo ma Eva?
print('Eva ma cislo {}'.format(zlateStranky['Eva']))