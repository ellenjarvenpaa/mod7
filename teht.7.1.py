kuukaudet = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukukuu", "Kesäkuu", "Heinäkuu",
              "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")

vuodenajat = ("Kevät", "Kesä", "Syksy", "Talvi")

järjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))

vuodenaika = kuukaudet, vuodenajat[järjestysnumero-1]

print (f"{järjestysnumero}. kuukausi on {vuodenaika}")