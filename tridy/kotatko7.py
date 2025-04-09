# Pridana metoda __str__(self)
# Jeji navratova hodnota je pouzita pri vypisu do konzole pomoci funkce print()
# Pri vypisu do konzole se nyni zobrazi "Kotatko Micka" nebo "Kotatko Mourek"


class Kotatko:
    def __init__(self, jmeno):
        print('Vytvarim kotatko jmenem {}'.format(jmeno))
        self.jmeno = jmeno
        
    def __str__(self):
        return 'Kotatko {}'.format(self.jmeno)

    def zamnoukej(self, zprava):
        print('{}: {}'.format(self.jmeno, zprava))

kotatko = Kotatko('Micka')
print(kotatko)
kotatko.zamnoukej('Mnau?')

jine_kotatko = Kotatko('Mourek')
print(jine_kotatko)
jine_kotatko.zamnoukej('Mnaaaaaaau!')
