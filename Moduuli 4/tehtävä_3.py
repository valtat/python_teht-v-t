numerot = []

while True:
    numero = input("Anna numero: ")
    if numero == "" : break
    try:
        fnum = float(numero)

    except:
        print("Väärä syöte")
        continue

    numerot.append(fnum)

suurin = max(numerot)
pienin = min (numerot)

print("Pienin numero on: ", pienin)
print("Suurin numero on: ", suurin)