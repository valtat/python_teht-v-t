class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
        self.aika = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        kuljettu_matka = self.nopeus * aika
        self.matka += kuljettu_matka
        self.aika += aika

    def tulosta_kuljettu_matka(self):
        print(self.rekisteritunnus, "on kulkenut", self.matka, "km.")


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


def luo_sähköauto(rekisteritunnus, huippunopeus, akkukapasiteetti):
    sähköauto = Sähköauto(rekisteritunnus, huippunopeus, akkukapasiteetti)
    return sähköauto


def luo_polttomoottoriauto(rekisteritunnus, huippunopeus, bensatankin_koko):
    polttomoottoriauto = Polttomoottoriauto(rekisteritunnus, huippunopeus, bensatankin_koko)
    return polttomoottoriauto


sähköauto = luo_sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = luo_polttomoottoriauto("ABC-123", 165, 32.3)

sähköauto.kiihdytä(100)
sähköauto.kulje(3)

polttomoottoriauto.kiihdytä(120)
polttomoottoriauto.kulje(3)

sähköauto.tulosta_kuljettu_matka()
polttomoottoriauto.tulosta_kuljettu_matka()
