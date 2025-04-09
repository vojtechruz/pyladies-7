# Abychom snadno rozeznali nekolik mnoukajicich kotatek, kazde kotatko nyni mnouka svym jmenem.
# V metode zamnoukej() nyni muzeme pristupovat k atributum instance pres self.
# self.jmeno pristupuje k atributu jmeno aktualni instance.


class Kotatko:
    def zamnoukej(self, zprava):
        print('{}: {}'.format(self.jmeno, zprava))


kotatko = Kotatko()
kotatko.jmeno = 'Micka'
kotatko.zamnoukej('Mnau?')
kotatko.zamnoukej('Mnau!!!!')

jine_kotatko = Kotatko()
jine_kotatko.jmeno = 'Mourek'
jine_kotatko.zamnoukej('Mnaaaaaaau!')
