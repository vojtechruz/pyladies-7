zlateStranky = {
    'Alice': '603888921',
    'Bohous':'777891776',
    'Cyril':'602345666',
    'Daniela':'728910000',
    'Eva':'777633798',
    'Filip':'608915433',
}

#Slovnik lze prochazet standardnim for-cyklem
#V takovem pripade for pouziva klice
print('Prochazeni pomoci standardniho foru prochazi jen klice')
for klic in zlateStranky:
    print(klic)

#stejneho efektu lze docilit zavolanim metody keys()
print('Prochazeni jen klicu pomoci zlateStranky.keys()')
for klic in zlateStranky.keys():
    print(klic)

#Pro prochazeni jen hodnot se da pouzit metoda values()
print('Prochazeni jen hodnot pomoci zlateStranky.values()')
for hodnota in zlateStranky.values():
    print(hodnota)

#Pokud je potreba oboje, lze pouzit metodu items(), ktera vraci dvojice (klic, hodnota)
print('Prochazeni dvojic klic-hodnota pomoci zlateStranky.items()')
for klic, hodnota in zlateStranky.items():
    print("[{}] = {}".format(klic, hodnota))


#Polozky nelze v prubehu prochazeni odebirat
for klic in zlateStranky.keys():
   del zlateStranky[klic]

#Pokud chces odebirat, musis toto pravidlo nejak obejit.
# Napriklad prevest klice na novy seznam a ten prochazet:
for klic in list(zlateStranky.keys()):
    if(klic == 'Filip'):
        del zlateStranky[klic]

# Overme si ze filip je opravdu odstranen
print('Zlate Stranky bez Filipa:')
print(zlateStranky)

#Ale lze je menit
for klic in zlateStranky.keys():
    zlateStranky[klic] = 'neco jineho'

print('Zlate stranky s upravenymi polozkami:')
print(zlateStranky)