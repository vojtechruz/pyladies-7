#Opakovani - seznamy
#Serazeny seznam prvku
seznamBarev = ['Cervena', 'Modra', 'Zelena', 'Fialova']
#Lze pridavat polozky
seznamBarev.append('Ruzova')
#Lze odebirat polozky
seznamBarev.remove('Modra')
#Pocet prvku seznamu pomoci funkce len()
print (len(seznamBarev))
print (seznamBarev)
#Lze pristupovat k prvku pomoci indexu, pocitame od 0
print ('Treti prvek v seznamu je {}'.format(seznamBarev[2]))


#Opakovani - N-tice
#Serazeny seznam prvky
#Nelze menit pocet prvku
nTiceJmenoVek = ('Leopold', 26)
print(nTiceJmenoVek)
#Lze pristupovat pres index jako u seznamu
print ('Druhy prvek n-tice je {}'.format(nTiceJmenoVek[1]))
