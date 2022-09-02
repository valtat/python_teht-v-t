import random
kokonaisluku = random.randint(1,10)
vastaus = int(input("Arvaa luku 1 ja 10 väliltä: "))

while vastaus != kokonaisluku:
    if vastaus > kokonaisluku:
        print("Liian iso")
        vastaus = int(input("Arvaa luku 1 ja 10 väliltä: "))
        
    elif vastaus < kokonaisluku:
        print("Liian pieni")
        vastaus = int(input("Arvaa luku 1 ja 10 väliltä: "))

print("Oikein!")


