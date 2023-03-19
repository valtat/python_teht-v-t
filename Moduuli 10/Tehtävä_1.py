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

hissi = Hissi(5,0)
hissi.siirry_kerrokseen(10)
hissi.siirry_kerrokseen(0)