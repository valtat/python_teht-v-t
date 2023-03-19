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
def luo_autot():
    autot = []
    for i in range(10):
        huippunopeus = random.randint(100, 200)
        autonNimi = f"ABC-{i + 1}"
        auto = Auto(autonNimi, huippunopeus)
        autot.append(auto)
    return autot

def kuljeta_autot(autot):
    for auto in autot:
        uusi_nopeus = random.randint(-10,15)
        auto.kiihdytä(uusi_nopeus)
        aika = 1
        auto.kulje(aika)
def tarkista_onko_kisa_käynnissä(autot):
    for auto in autot:
        kuljettu_matka = auto.matka
        if kuljettu_matka >= 10000:
            return False
    return True

def tulosta_autojen_tiedot():
    taulu = PrettyTable(["Rekisterinumero", "Huippunopeus", "Nopeus", "Matka", "Aika"])
    for auto in autot:
        taulu.add_row([auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka, auto.aika])
    print(taulu)

kisaKäynnissä = True
autot = luo_autot()

while kisaKäynnissä:

    kuljeta_autot(autot)
    kisaKäynnissä = tarkista_onko_kisa_käynnissä(autot)

tulosta_autojen_tiedot()
