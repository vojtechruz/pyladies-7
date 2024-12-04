class Zviratko:
    def __init__(self, nove_jmeno):
        self.jmeno = nove_jmeno

    def spi(self):
        print("Jdu spat.")

    def vydej_zvuk(self, zprava):
        print(self.jmeno + " : " + zprava)

    def sezer(self, jidlo):
        print("Zeru "+jidlo+" a moc mi chutna")


class Kotatko(Zviratko):

    def __init__(self, nove_jmeno, je_mlsne=False):
        super().__init__(nove_jmeno)

        self.je_mlsne = je_mlsne
        if je_mlsne:
            self.oblibena_jidla = ["kaviar", "lanyze", "humr"]


    def __str__(self):
        return "Kotatko jmenem " + self.jmeno

    def pred(self):
        print("Vrrrrrrr!")

    def sezer(self, jidlo):
        if self.je_mlsne:
            if jidlo in self.oblibena_jidla:
                self.vydej_zvuk("Jdu jist")
                super().sezer(jidlo)
            else:
                print("Fuj, ja bych radeji "+self.oblibena_jidla[0])




class Stenatko(Zviratko):

    def __str__(self):
        return "Stenatko jmenem " + self.jmeno

    def aportuj(self, vec):
        print("Aportuji " + vec)

class MlsneKotatko(Kotatko):
    def __init__(self, nove_jmeno):
        super().__init__(nove_jmeno)
        self.oblibena_jidla = ["kaviar", "lanyze", "humr"]

    def sezer(self, jidlo):
        if jidlo in self.oblibena_jidla:
            self.vydej_zvuk("Jdu jist")
            super().sezer(jidlo)
        else:
            print("Fuj, ja bych radeji "+self.oblibena_jidla[0])


fousek = Kotatko("Fousek")
fousek.vydej_zvuk("Chce se mi spat")
fousek.sezer("Mysicka")

mlsoun = Kotatko("Mlsoun", True)
mlsoun.vydej_zvuk("Dej mi neco lahodneho")
mlsoun.sezer("rohlik")
mlsoun.sezer("kaviar")

print(fousek)
