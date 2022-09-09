import random
tahkot = int(input("Syötä nopan tahkojen määrä: "))
noppa = 0
def nopanheitto(tahkot):
    return random.randint(1,tahkot)

while noppa != tahkot:
    noppa = nopanheitto(tahkot)
    print(noppa)