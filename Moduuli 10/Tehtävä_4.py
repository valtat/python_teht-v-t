import random
from prettytable import PrettyTable


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


class Kilpailu:
    def __init__(self, nimi, pituus, osallistujat):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = osallistujat

    def tunti_kuluu(self):
        for auto in self.osallistujat:
            uusi_nopeus = random.randint(-10, 15)
            auto.kiihdytä(uusi_nopeus)
            aika = 1
            auto.kulje(aika)

    def tulosta_tilanne(self):
        taulu = PrettyTable(["Rekisterinumero", "Huippunopeus", "Nopeus", "Matka", "Aika"])
        for auto in self.osallistujat:
            taulu.add_row([auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka, auto.aika])
        print(taulu)

    def kilpailu_ohi(self):
        for auto in self.osallistujat:
            kuljettu_matka = auto.matka
            if kuljettu_matka >= self.pituus:
                return True
        return False
    
    
def luo_autot(määrä):
    autot = []
    for i in range(määrä):
        huippunopeus = random.randint(100, 200)
        auton_nimi = f"ABC-{i + 1}"
        auto = Auto(auton_nimi, huippunopeus)
        autot.append(auto)
    return autot


kilpailu_ohi = False
autot = luo_autot(10)
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
kuluneet_tunnit = 0

while not kilpailu_ohi:

    kilpailu.tunti_kuluu()
    kilpailu_ohi = kilpailu.kilpailu_ohi()
    kuluneet_tunnit += 1
    if kuluneet_tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()
