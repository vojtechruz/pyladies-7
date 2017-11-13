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
for klic in zlateStranky:
    print(klic)

#stejneho efektu lze docilit zavolanim metody keys()
for klic in zlateStranky.keys():
    print(klic)

#Pro prochazeni jen hodnot se da pouzit metoda values()
for hodnota in zlateStranky.values():
    print(hodnota)

#Pokud je potreba oboje, lze pouzit metodu items(), ktera vraci dvojice (klic, hodnota)
for klic, hodnota in zlateStranky.items():
    print("[{}] = {}".format(klic, hodnota))


#Polozky nelze v prubehu prochazeni odebirat
for klic in zlateStranky.keys():
   del zlateStranky[klic]

#Ale lze je menit
for klic in zlateStranky.keys():
    zlateStranky[klic] = 'neco jineho'

print(zlateStranky)