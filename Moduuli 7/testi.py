#Esimerkkejä:
#lisää Maija
#poista Maija
#lopeta

henkilöt = set()

syöte = input("Anna nimi tai lopeta tyhjällä merkkijonolla: ")
sanat = syöte.split()
komento = sanat[0]
if len(komento)>=1:
    kohde = sanat[1]

while komento != "lopeta":
    if komento=="lisää":
        if kohde in henkilöt:
            print(f"{kohde} on jo lisätty.")
        else:
            henkilöt.add(kohde)
    elif komento=="poista":
        if kohde in henkilöt:
            henkilöt.remove(kohde)
        else:
            print(f"{kohde} ei esiinny joukossa.")
    else:
        print("Virheellinen nimi.")
    syöte = input("Anna seuraava komento: ")
    sanat = syöte.split()
    komento = sanat[0]
    if len(sanat) >= 2:
        kohde = sanat[1]
