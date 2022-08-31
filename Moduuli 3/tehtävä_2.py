hyttiluokka = input("Anna hyttiluokkasi LUX/A/B/C: ")

if hyttiluokka != "A" and hyttiluokka != "B" and hyttiluokka != "C" and hyttiluokka != "LUX":
    print("Virheellinen hyttiluokka.")

elif hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")

elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")

else:
    print("C on ikkunaton hytti autokannen alapuolella.")

