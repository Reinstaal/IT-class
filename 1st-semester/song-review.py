songbewertung = {
    "DON'T TOUCH MY CLOGS": "5★",
    "ROLL OUT THE FALLOUT!": "4★",
    "DIM SUM PARADISE": "5★"
}

def anzeigen_alphabet():
    for w in sorted(songbewertung):
        print(w, songbewertung[w])


def anzeigen_bewertung():
    for w in sorted(songbewertung, key=songbewertung.get, reverse=True):
        print(w, songbewertung[w])


def hinzufuegen():
    anzeigen_alphabet()
    titel = input("Geben Sie bitte den Titel ein, den Sie hinzufügen möchten\n")
    bewertung = input(f"Wie bewerten Sie {titel}?\n")
    songbewertung[titel] = bewertung + "★"


def bearbeiten():
    anzeigen_alphabet()
    titelold = input("Geben Sie bitte den Titel ein, den Sie bearbeiten möchten\n")
    titelnew = input("Geben Sie bitte den neuen Titel ein\n")
    bewertung = input("Geben Sie bitte die neue Bewertung ein\n")
    del songbewertung[titelold]
    songbewertung[titelnew] = bewertung


def entfernen():
    anzeigen_alphabet()
    titelkill = input("Geben Sie bitte den Titel ein, den Sie entfernen möchten\n")
    del songbewertung[titelkill]


def suche():
    w = input("Bitte den gesuchten Titel eingeben\n")
    if w in songbewertung:
        print(w, songbewertung[w])
    else:
        print("Gesuchter Titel wurde nicht gefunden.\n")
    # print(songbewertung.__contains__(w))


while True:
    print("""
1 - Alle Songs anzeigen
2 - Song hinzufügen oder bearbeiten
3 - Song löschen
4 - Song nach Titel suchen
5 - Songs nach Bewertung anzeigen
9 - Beenden""")

    auswahl = input("\nBitte Funktion auswählen:\n")

    match auswahl:
        case "1":
            anzeigen_alphabet()
            #zeige dic an in alphabetisch blabla
        case "2":
            auswahl = input("""
1 - Song hinzufügen
2 - Song bearbeiten
9 - Zurück zum Menü""")
            match auswahl:
                case "1":
                    hinzufuegen()
                case "2":
                    bearbeiten()
                case _:
                    break
        case "3":
            entfernen()
        case "4":
            suche()
        case "5":
            anzeigen_bewertung()
        case "9":
            break
        case _:
            print("Ungültige Eingabe.\n")