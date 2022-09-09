import random
noppa = 0
def nopanheitto():
    return random.randint(1,6)

while noppa < 6:
    noppa = nopanheitto()
    print(noppa)