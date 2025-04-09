# Rozsirena verze tridy Kotatko. Metoda zamnokej() nyni prima parametr zprava.
# Pri kazdem zavolani metody se predava, co presne ma kotatko zamnoukat.


class Kotatko:
    def zamnoukej(self, zprava):
        print('Kotatko: {}'.format(zprava))


kotatko = Kotatko()
kotatko.zamnoukej('Mnau?')
kotatko.zamnoukej('MNAAAAAAAAAU!')
