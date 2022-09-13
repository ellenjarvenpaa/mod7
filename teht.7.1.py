kuukaudet = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukukuu", "Kesäkuu", "Heinäkuu",
              "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")

vuodenajat = ("Kevät", "Kesä", "Syksy", "Talvi")

järjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))

if järjestysnumero == kuukaudet[11:1]:
    print(vuodenajat[3])

if järjestysnumero == kuukaudet[2:4]:
    print(vuodenajat[0])

if järjestysnumero == kuukaudet[5:7]:
    print(vuodenajat[1])

if järjestysnumero == kuukaudet[8:10]:
    print(vuodenajat[2])