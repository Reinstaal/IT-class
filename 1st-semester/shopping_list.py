artikel = []
menge = []

def hinzufuegen():
    n_artikel = str(input("Geben Sie bitte den Artikel ein, den Sie hinzufügen möchten:\n"))
    artikel.append(n_artikel)
    n_menge = int(input("Geben Sie bitte die Menge des Artikels ein\n"))
    menge.append(n_menge)


def entfernen():
    r_artikel = str(input("Geben Sie bitte den Artikel an, den Sie entfernen möchten:\n"))
    # setzt r_menge als index (zählerposition) von eingegebenem Artikel fest
    r_menge = int(artikel.index(r_artikel))
    artikel.remove(r_artikel)
    # del löscht nach index: Lösche in der Liste "menge" die Position von der Zahl "r_menge"
    del menge[r_menge]


def anzeigen():
    print()
    for i in range(len(artikel)):
        print(f"{artikel[i]}: {menge[i]}x")


while True:
    auswahl = int(input("""\nWillkommen bei Ihrer persönlichen Einkaufsliste!
        0 = Artikel hinzufügen
        1 = Artikel entfernen
        2 = Einkaufsliste anzeigen
        3 = Einkaufsliste beenden\n"""))
    match auswahl:
        case 0:
            hinzufuegen()
        case 1:
            entfernen()
        case 2:
            anzeigen()
        case 3:
            break
        case _:
            print("Ungültige Wahl!")