import random
N = 1000000
n = 0
toistot = 0

while toistot < N:
    #arvo x välillä -1 ja 1
    x = random.randint(-1,1)
    #arvo y välillä -1 ja 1
    y = random.randint(-1,1)
    # osuuko x ja y ympyrän sisälle?

    if (x * x + y * y < 1):
        n += 1

pi = 4 * n / N

print(f"Piin likiarvo on {pi}")