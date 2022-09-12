asemat = {}

kysymys = input("Valitse tominta (Syöttö / Haku / Lopeta)\n")

if kysymys == "Syöttö":
    ICAO = input("Syötä ICAO koodi\n")
    nimi = input("Syötä nimi\n")
    asemat[ICAO] = nimi

kysymys = input("Valitse tominta Syöttö / Haku / Lopeta\n")

if kysymys == "Haku":
    koodi = input("Syötä ICAO koodi\n")
    print(f"{koodi}, {asemat[ICAO]}")

kysymys = input("Valitse tominta Syöttö / Haku / Lopeta\n")

if kysymys == "Lopeta":
    print("Ohjelma loppuu")
