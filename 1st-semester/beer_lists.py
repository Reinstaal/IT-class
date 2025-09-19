# Festlegen der Listen
zutaten = ["Hopfen", "Gerste", "Malz", "Wasser", "Apfelsaft", "Bananensaft"]
mengen = [100, 200, 300, 400, 500, 1000]

while True:
    # Benutzer nach der Menge fragen
    anzahl = float(input("Geben Sie die gewünschte Menge zum Brauen ein\n"))

    # Mengen der Zutaten entsprechend der angegebenen Menge ausgeben
    print('\nEINZELNE PRINTS\n')
    print(f"{zutaten[0]}: {mengen[0] * anzahl} mg/mgl")
    print(f"{zutaten[1]}: {mengen[1] * anzahl} mg/mgl")
    print(f"{zutaten[2]}: {mengen[2] * anzahl} mg/mgl")
    print(f"{zutaten[3]}: {mengen[3] * anzahl} mg/mgl")

    # oder
    print('\nSCHLEIFE\n')
    for i in range(len(zutaten)):
        print(f"{zutaten[i]}: {mengen[i] * (anzahl)} mg/ml")

    #neue Zutat
    n_zutat = input("\nWelche neue Zutat möchten Sie hinzufügen?    ")
    zutaten.append(n_zutat)
    n_mengen = int(input("Wie hoch ist die Menge der neuen Zutat?    "))
    mengen.append(n_mengen)

    #entfernen Zutat
    r_zutat = input("\nWelche Zutat möchten Sie entfernen?    ")
    zutaten.remove(r_zutat)
    r_mengen = int(input("Wie hoch ist die hierfür bestimmte Menge?"))
    mengen.remove(n_mengen)
