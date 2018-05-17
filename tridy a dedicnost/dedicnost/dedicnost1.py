# Trida Kotatko
# Kazde kotatko ma jmeno a umi jist a mnoukat

class Kotatko:
    def __init__(self, jmeno):
        print('Vytvarim kotatko jmenem {}'.format(jmeno))
        self.jmeno = jmeno

    def __str__(self):
        return 'Kotatko {}'.format(self.jmeno)

    def snez(self, jidlo):
        print('{}: Mnam! {} mi velmi chutna.'.format(self.jmeno, jidlo))

    def zamnoukej(self, zprava):
        print('{}: {}'.format(self.jmeno, zprava))


kotatko = Kotatko('Micka')
kotatko.zamnoukej('Mnau?')
kotatko.snez('Mys')
