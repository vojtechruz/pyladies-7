# Mlsne kotatko nyni mnouka jinak nez bezna kotatka.
# Pomoci super() lze volat metody na predkovi, v tomto pripade volame zamnoukej() na tride Kotatko.
# Pri volani muzeme predat libovolny parametr.
# Zde predavame puvodni zpravu, ale pridame k ni dovetek "Mam chut na neco dobreho."

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

    def zamnoukej(self, zprava):
        super().zamnoukej("{} Mam chut na neco dobreho.".format(zprava))


class Stenatko(Zviratko):
    def __str__(self):
        return 'Stenatko {}'.format(self.jmeno)

    def zastekej(self, zprava):
        print('{}: Haf! {}'.format(self.jmeno, zprava))


kotatko = Kotatko('Micka')
kotatko.zamnoukej('Ta vaza spadla sama!')
kotatko.snez('Mys')

mlsne_kotatko = MlsneKotatko('Mlsoun')
mlsne_kotatko.zamnoukej('Uz jsem dlouho nejedl.')
mlsne_kotatko.snez('Mys')

stenatko = Stenatko('Rex')
stenatko.zastekej('Ta louzicka uz tu byla!')
stenatko.snez('Kost')
