luku = int(input("Syötä kokonaisluku: "))

if luku <= 1:
    print(luku, "ei ole alkuluku.")
else:
    for i in range(2,luku):
        if(luku % i) == 0:
            print(luku, "ei ole alkuluku.")
            break
    else:
        print(luku, "on alkuluku.")