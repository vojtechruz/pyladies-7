# Nyni vytvorime tridu Stenatko.
# Stenatko je v necem podobne kotatku a v necem se lisi. Obe mladatka umi jist.
# Metoda snez() je duplikovana v kotatku i stenatku.

class Kotatko:
    def __init__(self, jmeno):
        print('Vytvarim kotatko jmenem {}'.format(jmeno))
        self.jmeno = jmeno

    def __str__(self):
        return 'Kotatko {}'.format(self.jmeno)

    def snez(self, jidlo):
        print('{}: Mnam! {} mi velmi chutna.'.format(self.jmeno, jidlo))

    def zamnoukej(self, zprava):
        print('{}: Mnau! {}'.format(self.jmeno, zprava))


class Stenatko:
    def __init__(self, jmeno):
        print('Vytvarim stenatko jmenem {}'.format(jmeno))
        self.jmeno = jmeno

    def __str__(self):
        return 'Stenatko {}'.format(self.jmeno)

    def snez(self, jidlo):
        print('{}: Mnam! {} mi velmi chutna.'.format(self.jmeno, jidlo))

    def zastekej(self, zprava):
        print('{}: Haf! {}'.format(self.jmeno, zprava))


kotatko = Kotatko('Micka')
kotatko.zamnoukej('Ta vaza spadla sama!')
kotatko.snez('Mys')

stenatko = Stenatko('Rex')
stenatko.zastekej('Ta louzicka uz tu byla!')
stenatko.snez('Kost')
