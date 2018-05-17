# Pridana trida MlsneKotatko, ktere dedi od tridy Kotatko.
# MlsneKotatko ma metodu snez(), kterou uz definuje jeji predek Zviratko (MlsneKotatko dedi od Kotatka a to dedi od Zviratka)
# Tim, ze definuje stejnou metodu jako predek, "prekryva" ji.
# Pri volani metody "snez()" na instanci mlsneho kotatka se nepouzije metoda snez() ze zviratka, ale ta z tridy MlsneKotatko.
# Stenatko metodu snez() neprekryva. Kdyz se zavola tato metoda na stenatku, pouzije se tedy metoda snez() ze zviratka.

class Zviratko:
    def __init__(self, jmeno):
        print('Vytvarim zviratko jmenem {}'.format(jmeno))
        self.jmeno = jmeno

    def snez(self, jidlo):
        print('{}: Mnam! {} mi velmi chutna.'.format(self.jmeno, jidlo))


class Kotatko(Zviratko):
    def __str__(self):
        return 'Kotatko {}'.format(self.jmeno)

    def zamnoukej(self, zprava):
        print('{}: Mnau! {}'.format(self.jmeno, zprava))


class MlsneKotatko(Kotatko):
    def __str__(self):
        return 'Mlsne Kotatko {}'.format(self.jmeno)

    def snez(self, jidlo):
        print('{}: Fuj! {} mi vubec nechutna. Ja radeji zverinu.'.format(self.jmeno, jidlo))


class Stenatko(Zviratko):
    def __str__(self):
        return 'Stenatko {}'.format(self.jmeno)

    def zastekej(self, zprava):
        print('{}: Haf! {}'.format(self.jmeno, zprava))


kotatko = Kotatko('Micka')
kotatko.zamnoukej('Ta vaza spadla sama!')
kotatko.snez('Mys')

mlsne_kotatko = MlsneKotatko('Mlsoun')
mlsne_kotatko.zamnoukej('Mam chut na neco dobreho!')
mlsne_kotatko.snez('Mys')

stenatko = Stenatko('Rex')
stenatko.zastekej('Ta louzicka uz tu byla!')
stenatko.snez('Kost')
