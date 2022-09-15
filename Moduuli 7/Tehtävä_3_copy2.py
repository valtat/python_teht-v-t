lentokentät = {}
input_description = ("Kirjoita 'lisää' lisätäksesi uuden lentokentän ja ICAO-koodin, "
"tai 'hae' hakeaksesi lentokenttää ICAO-koodin perusteella. "
"Voit lopettaa ohjelman suorituksen tyhjällä merkkijonolla: ")
syöte = input(input_description)

while syöte != "":
    if syöte == "lisää":
        koodi = input("Anna lentokentän ICAO-koodi: ")
        if koodi in lentokentät:
            print("Koodi on jo olemassa.")
        nimi = input("Anna lentokentän nimi: ")
        lentokentät[koodi] = nimi
    if syöte == "hae":
        haku = input("Hae lentokenttää ICAO-koodin avulla: ")
        if haku in lentokentät:
            print(f"ICAO-koodia {haku} vastaava lentokenttä on {lentokentät[haku]}.")
    syöte = input(input_description)