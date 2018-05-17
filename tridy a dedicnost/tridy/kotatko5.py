# Tride Kotatko jsme nyni pridali konstruktor - __init__(self, jmeno).
# V kontstruktoru nastavujeme hodnotu atributu 'jmeno' z parametru 'jmeno' predaneho do konstruktoru.
# Puvodni zpusob nastavovani atributu z minuleho prikladu je zakomentovan.

class Kotatko:
    def __init__(self, jmeno, barva, vek):
        print('Vytvarim kotatko se jmenem {}'.format(jmeno))
        self.jmeno = jmeno
        self.barva = barva
        self.vek = vek

    def zamnoukej(self, zprava):
        print('{}: {}'.format(self.jmeno, zprava))

    def __str__(self):
        return "Kotatko jmenem:"+self.jmeno;

kotatko = Kotatko("Micka", "Hneda", 2)
print(kotatko)
# kotatko.jmeno = 'Micka'
# kotatko.zamnoukej('Mnau?')
