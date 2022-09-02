tunnus = ""
salasana = ""
yritykset = 0

while not (tunnus == "python" and salasana == "rules") and yritykset <= 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    yritykset = yritykset + 1

if (yritykset >= 5):
    print("Pääsy evätty.")
else:
    print("Tervetuloa!")