vuodenaika = {"talvi": (1, 2, 12),
             "kevät": (3, 4, 5),
             "kesä": (6, 7, 8),
             "syksy": (9, 10, 11)}

kuukausinumero = int(input("Anna kuukauden numero (1-12): "))

for avain in vuodenaika.keys():
    numerot = vuodenaika[avain]
    if kuukausinumero in numerot:
        print(f"{kuukausinumero}. kuukausi on {avain}.")