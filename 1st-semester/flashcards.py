import random
lernkarten = {
    "Noll": "0",
    "Ett":  "1",
    "Tva":  "2",
    "Tre":  "3",
}

while True:
    auswahl = int(input("""Optionen:"
          1: Lernkarte anzeigen
          2: Neue Lernkarte hinzufügen
          3: Lernkarte löschen
          4: Lernen (zufällige Karte)
          5: Programm beenden\n"""))

    match auswahl:
        case 1:
            begriff = input("Gib den Begriff ein:\n")
            if begriff in lernkarten:
                print(f"{lernkarten[begriff]}")
            else:
                print("Begriff wurde nicht erkannt.\n")

        case 2:
            n_lernkarten = input("Bitte geben Sie die Lernkarte ein, die Sie hinzufügen möchten:\n")
            if n_lernkarten in lernkarten:
                print("Begriff existiert schon, bitte zuerst entfernen!")
                continue
            n_definition = input("Bitte geben Sie die Lösung der Lernkarte an:\n")
            if n_definition in lernkarten.values():
                print("Definition existiert schon, bitte zuerst entfernen!")
                continue
            lernkarten[n_lernkarten] = n_definition
            print(f"Lernkarte '{n_lernkarten}' mit der Definition '{n_definition}' wurde hinzugefügt.")

        case 3:
            r_lernkarten = input("Bitten geben Sie die Lernkarte ein, die Sie entfernen möchten:\n")
            try:
                del lernkarten[r_lernkarten]
                print(f"Begriff '{r_lernkarten}' wurde um die Ecke gebracht.")
            except:
                print("Begriff wurde nicht in den Lernkarten gefunden!")

        case 4:
            if bool(lernkarten):
                while True:
                    f_lernen = random.choice(list(lernkarten))
                    definition = lernkarten[f_lernen]
                    a_lernen = input(f"Was ist {f_lernen}?\n")
                    # match a_lernen:
                    #     case "n":
                    #         break
                    #     case definition:
                    #         print("Super, das ist richtig!\n")
                    #     case _:
                    #         print(f"Falsch, die richtige Antwort ist {definition}. Mit 'n' können Sie das Lernen beenden.")
                    if a_lernen == "n":
                        break
                    if definition == a_lernen:
                        print("Super, das ist richtig!\n")
                    else:
                        print(f"Falsch, die richtige Antwort ist {definition}. Mit 'n' können Sie das Lernen beenden.")
            else:
                print()
        case 5:
            break

        case _:
            print("Ungültige Eingabe! D:")