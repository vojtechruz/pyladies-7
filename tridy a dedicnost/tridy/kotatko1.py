# Jednoducha verze tridy kotatko, s metodou zamnoukej(). Vsechny kotatka zatim mnoukaji stejne.
#
# - trida Zviratko
# - Ma alespon jeden atribut nastaveny v kosntruktoru
# - ma alespon jednu metodou
# - bonus - methoda na prevod na retezec
# - vytvorit instanci a zavolat na ni metodu

class Jehnatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __str__(self):
        return "Ja jsem male rozkosne jehne "+self.jmeno

    def udelejZvukCoDelajiJehnatka(self):
        print(self.jmeno + ": MEeeee?")

jehne = Jehnatko('Rudolf')
print(jehne)
jehne.udelejZvukCoDelajiJehnatka()

zcelaJineJehne = Jehnatko('Karel')
zcelaJineJehne.udelejZvukCoDelajiJehnatka()
