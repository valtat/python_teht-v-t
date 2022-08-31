sukupuoli = (input("Anna sukupuolesi: "))
hemoglobiini = int(input("Anna hemoglobiiniarvosi: "))

if sukupuoli == "Mies" or sukupuoli == "mies" or sukupuoli == "MIES":
    if hemoglobiini >= 134 and hemoglobiini <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemoglobiini < 134:
        print("Hemoglobiiniarvosi on matala.")
    elif hemoglobiini > 195:
        print ("Hemoglobiiniarvosi on korkea.")

if sukupuoli == "Nainen" or sukupuoli == "nainen" or sukupuoli == "NAINEN":
    if hemoglobiini >= 117 and hemoglobiini <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemoglobiini < 117:
        print("Hemoglobiiniarvosi on matala.")
    elif hemoglobiini > 175:
        print ("Hemoglobiiniarvosi on korkea.")