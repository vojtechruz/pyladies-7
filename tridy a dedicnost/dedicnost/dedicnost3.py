# Pridana nova trida Zviratko.
# Kotatko i stenatko dedi od tridy Zviratko.
# Metoda snez() byla presunuta z Kotatka a Stenatka do spolecneho predka - tridy Zviratko.
# Na kotatku i stenatku lze stale volat metodu snez(), vola se ta z predka.


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


class Stenatko(Zviratko):
    def __str__(self):
        return 'Stenatko {}'.format(self.jmeno)

    def zastekej(self, zprava):
        print('{}: Haf! {}'.format(self.jmeno, zprava))


kotatko = Kotatko('Micka')
kotatko.zamnoukej('Ta vaza spadla sama!')
kotatko.snez('Mys')

stenatko = Stenatko('Rex')
stenatko.zastekej('Ta louzicka uz tu byla!')
stenatko.snez('Kost')
