gallona = int(input("Syötä gallonien määrä tai lopeta negatiivisella: "))

def muunna_litroiksi(gallona):
    return gallona * 3.78541178

while gallona > -1:
    litrat = muunna_litroiksi(gallona)
    print(f"{gallona:d} gallonaa on {litrat:.2f} litraa.")
    gallona = int(input("Syötä gallonien määrä tai lopeta negatiivisella: "))