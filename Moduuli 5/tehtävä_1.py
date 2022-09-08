import random
noppa = int(input("Kuinka monta noppaa heitetään?: "))
for i in range(noppa):
    arpa = random.randint(1,6)

summa = (arpa*noppa)
print("Noppien summa: ", summa)
