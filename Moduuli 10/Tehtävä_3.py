class Hissi:
    YLÖS = "Ylös"
    ALAS = "Alas"

    def __init__(self, ylin_kerros, alin_kerros):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.nykyinen_kerros = self.alin_kerros

    def siirry_kerrokseen(self, haluttu_kerros):
        liiketekijät = self.laske_liiketekijät(self.nykyinen_kerros, haluttu_kerros)
        liikuttavien_kerrosten_määrä = liiketekijät[0]
        suunta = liiketekijät[1]
        for i in range(liikuttavien_kerrosten_määrä):
            if suunta == self.YLÖS:
                self.kerros_ylös()
            if suunta == self.ALAS:
                self.kerros_alas()

    def laske_liiketekijät(self, nykyinen_kerros, haluttu_kerros):
        liikuttavien_kerrosten_määrä = nykyinen_kerros - haluttu_kerros
        if liikuttavien_kerrosten_määrä < 0:
            suunta = self.YLÖS
        if liikuttavien_kerrosten_määrä > 0:
            suunta = self.ALAS
        return (abs(liikuttavien_kerrosten_määrä), suunta)

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Saavuit kerrokseen {self.nykyinen_kerros}.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Saavuit kerrokseen {self.nykyinen_kerros}.")


class Talo:
    def __init__(self, ylinKerros, alinKerros, hissienMäärä):
        self.ylinKerros = ylinKerros
        self.alinKerros = alinKerros
        self.hissienMäärä = hissienMäärä
        self.hissit = []
        for i in range(hissienMäärä):
            hissi = Hissi(ylinKerros, alinKerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissinro, kohdekerros):
        self.hissinro = hissinro
        self.kohdekerros = kohdekerros
        hissi = self.hissit[hissinro]
        hissi.siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alinKerros)

lista = [0,1,2,3]
talo1 = Talo(5, 1, 2)
talo1.aja_hissiä(1, 5)
talo1.aja_hissiä(0, 3)
talo1.palohälytys()
