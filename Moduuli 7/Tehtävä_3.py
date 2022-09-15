lentokentät = {}
syöte = input("Kirjoita 'lisää' lisätäksesi uuden lentokentän ja ICAO-koodin, tai 'hae' hakeaksesi lentokenttää ICAO-koodin perusteella. Voit lopettaa ohjelman suorituksen tyhjällä merkkijonolla: ")

while syöte != "":
    if syöte == "lisää":
        syöte = input("Anna lentokentän ICAO-koodi: ")
        if syöte in lentokentät:
            print("Koodi on jo olemassa.")
        nimi = input("Anna lentokentän nimi: ")
        lentokentät[syöte] = nimi
        syöte = input("Kirjoita 'lisää' lisätäksesi uuden lentokentän ja ICAO-koodin, tai 'hae' hakeaksesi lentokenttää ICAO-koodin perusteella. Voit lopettaa ohjelman suorituksen tyhjällä merkkijonolla: ")
    if syöte == "hae":
        syöte = input("Hae lentokenttää ICAO-koodin avulla: ")
        if syöte in lentokentät:
            print(f"ICAO-koodia {syöte} vastaava lentokenttä on {lentokentät[syöte]}.")
            syöte = input(
                "Kirjoita 'lisää' lisätäksesi uuden lentokentän ja ICAO-koodin, tai 'hae' hakeaksesi lentokenttää ICAO-koodin perusteella. Voit lopettaa ohjelman suorituksen tyhjällä merkkijonolla: ")