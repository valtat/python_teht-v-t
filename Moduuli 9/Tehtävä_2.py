class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus on {auto.rekisteritunnus} ja huippunopeus on {auto.huippunopeus}km/h.")
print(f"Auton nopeus on {auto.nopeus}km/h ja kuljettu matka on {auto.matka}km.")

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Auton nopeus on {auto.nopeus}km/h.")
auto.kiihdytä(-200)
print(f"Auton nopeus on {auto.nopeus}km/h.")