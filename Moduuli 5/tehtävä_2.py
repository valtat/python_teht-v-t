luvut = []
luku = " "

while luku != "":
    luku = input("Syötä lukuja ja lopeta syöttämällä tyhjä: ")
    if luku != "":
        luvut.append(int(luku))

luvut.sort(reverse=True)
print(luvut[:5])