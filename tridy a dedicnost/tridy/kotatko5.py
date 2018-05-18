# Tride Kotatko jsme nyni pridali konstruktor - __init__(self, jmeno).
# V kontstruktoru nastavujeme hodnotu atributu 'jmeno' z parametru 'jmeno' predaneho do konstruktoru.
# Puvodni zpusob nastavovani atributu z minuleho prikladu je zakomentovan.

class Kotatko:
    def __init__(self, jmeno):
        print('Vytvarim kotatko se jmenem {}'.format(jmeno))
        self.jmeno = jmeno

    def zamnoukej(self, zprava):
        print('{}: {}'.format(self.jmeno, zprava))


kotatko = Kotatko('Micka')
# kotatko.jmeno = 'Micka'
kotatko.zamnoukej('Mnau?')

jine_kotatko = Kotatko('Mourek');
# jine_kotatko.jmeno = 'Mourek'
jine_kotatko.zamnoukej('Mnaaaaaaau!')
