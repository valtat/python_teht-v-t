henkilöt = set()

nimi = input("Anna nimi tai lopeta tyhjällä merkkijonolla: ")

while nimi != "":
    if nimi in henkilöt:
        print("Aiemmin syötetty nimi.")
    else:
        henkilöt.add(nimi)
        print("Uusi nimi lisätty.")

    nimi = input("Anna seuraava nimi tai lopeta tyhjällä merkkijonolla: ")

for h in henkilöt:
    print(h)