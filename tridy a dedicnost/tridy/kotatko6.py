# Trida Kotatko zustava stejna.
# Kdyz zkusime vypsat instanci tridy Kotatko pomoci print() do konzole, vystup neni zcela idealni...

class Kotatko:
    def __init__(self, jmeno):
        print('Vytvarim kotatko jmenem {}'.format(jmeno))
        self.jmeno = jmeno

    def zamnoukej(self, zprava):
        print('{}: {}'.format(self.jmeno, zprava))


kotatko = Kotatko('Micka')
print(kotatko)
kotatko.zamnoukej('Mnau?')

jine_kotatko = Kotatko('Mourek');
print(jine_kotatko)
jine_kotatko.zamnoukej('Mnaaaaaaau!')
