vuodenajat = ("Talvi","Talvi","Kevät","Kevät","Kevät","Kesä","Kesä","Kesä","Syksy","Syksy","Syksy","Talvi")
kuukausinumero = int(input("Anna kuukauden numero (1-12): "))
vuodenaika = vuodenajat[kuukausinumero-1]
print (f"{kuukausinumero}. kuukausi on {vuodenaika}.")