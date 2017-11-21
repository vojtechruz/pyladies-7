#Opakovani - seznamy
#Serazeny seznam prvku
seznam_barev = ['Cervena', 'Modra', 'Zelena', 'Fialova']
#Lze pridavat polozky
seznam_barev.append('Ruzova')
#Lze odebirat polozky
seznam_barev.remove('Modra')
#Pocet prvku seznamu pomoci funkce len()
print (len(seznam_barev))
print (seznam_barev)
#Lze pristupovat k prvku pomoci indexu, pocitame od 0!
print ('Treti prvek v seznamu je {}'.format(seznam_barev[2]))


#Opakovani - N-tice
#Serazeny seznam prvky
#Nelze menit pocet prvku
ntice_jmeno_vek = ('Leopold', 26)
print(ntice_jmeno_vek)
#Lze pristupovat pres index jako u seznamu
print ('Druhy prvek n-tice je {}'.format(ntice_jmeno_vek[1]))
