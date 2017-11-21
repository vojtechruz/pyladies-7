zlate_stranky = {
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
for klic in zlate_stranky:
    print(klic)

#stejneho efektu lze docilit zavolanim metody keys()
print('Prochazeni jen klicu pomoci zlate_stranky.keys()')
for klic in zlate_stranky.keys():
    print(klic)

#Pro prochazeni jen hodnot se da pouzit metoda values()
print('Prochazeni jen hodnot pomoci zlate_stranky.values()')
for hodnota in zlate_stranky.values():
    print(hodnota)

#Pokud je potreba oboje, lze pouzit metodu items(), ktera vraci dvojice (klic, hodnota)
print('Prochazeni dvojic klic-hodnota pomoci zlate_stranky.items()')
for klic, hodnota in zlate_stranky.items():
    print("[{}] = {}".format(klic, hodnota))


#Polozky nelze v prubehu prochazeni odebirat
for klic in zlate_stranky.keys():
   del zlate_stranky[klic]

#Pokud chces odebirat, musis toto pravidlo nejak obejit.
# Napriklad prevest klice na novy seznam a ten prochazet:
for klic in list(zlate_stranky.keys()):
    if(klic == 'Filip'):
        del zlate_stranky[klic]

# Overme si ze filip je opravdu odstranen
print('Zlate Stranky bez Filipa:')
print(zlate_stranky)

#Ale lze je menit
for klic in zlate_stranky.keys():
    zlate_stranky[klic] = 'neco jineho'

print('Zlate stranky s upravenymi polozkami:')
print(zlate_stranky)