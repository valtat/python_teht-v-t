LUOTI = 13.3
NAULA = 32 * LUOTI
LEIVISKÄ = 20 * NAULA


leiviskät_str = input("Anna leiviskät: ")
leiviskät = float(leiviskät_str) * LEIVISKÄ
naulat_str = input("Anna naulat: ")
naulat = float(naulat_str) * NAULA
luodit_str = input("Anna luodit: ")
luodit = float(luodit_str) * LUOTI

tulos = (leiviskät + naulat + luodit)
kilot = int(tulos / 1000)
print("Massa nykymittojen mukaan:\n" + str(kilot) + " kilogrammaa ja", str(round(tulos%1000, 2)) + " grammaa.")