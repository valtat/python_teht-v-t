tuuma = int(input("Anna tuuma: "))
senttimetri = float(2.54)

while tuuma > 0:
    print(f"{tuuma:d} tuumaa on {tuuma * senttimetri:.2f} senttimetriä")
    tuuma = int(input("Anna tuuma: "))