nimet = set()

nimi = input("Kirjoita nimi")
while nimi != "":
    if nimi in nimet:
        print(f"{nimi} on aiemmin syötetty nimi")
    elif nimi != nimet:
        nimet.add(nimi)
        print(f"{nimi} on uusi nimi")
    nimi = input("Kirjoita nimi")

print("Kaikki nimet:")
for n in nimet:
    print(n)
