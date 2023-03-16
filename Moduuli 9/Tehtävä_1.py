class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus on {auto.rekisteritunnus} ja huippunopeus on {auto.huippunopeus}km/h.")
print(f"Auton nopeus on {auto.nopeus}km/h ja kuljettu matka on {auto.matka}km.")