buecher = ["Harry","Potter","Voldemort Teil 3", "Oh Bruder im Himmel"]


def anzeigen():
    if len(buecher) > 0:
        print("\nBücher im Regal:")
        for i in range(len(buecher)):
            print(f"{i+1}. {buecher[i]}")
    else:
        print("\nRegal ist leer!")


def suchen():
    if len(buecher) > 0:
        w = input("\nBitte den gesuchten Titel eingeben: ")
        if w in buecher:
            print(w, "ist vorhanden!")
        else:
            print("\nGesuchter Titel wurde nicht gefunden.")
    else:
        print("\nOffensichtlich ist das Regal leer, wonach möchten Sie denn da suchen?")


def hinzufuegen():
    n_buch = input("\nGeben Sie bitte den Buchtitel ein, den Sie hinzufügen möchten: ")
    if n_buch != "":
        buecher.append(n_buch)
        print("\n" + n_buch, "wurde dem regal hinzugefügt.")
    else:
        print("\nFehler: Titel darf nicht leer sein!")


def entfernen():
    if len(buecher) > 0:
        anzeigen()
        r_buch = input("\nGeben Sie bitte den Buchtitel an, den Sie entfernen möchten: ")
        try:
            buecher.remove(r_buch)
            print("\n" + r_buch, "wurde entfernt.")
        except ValueError:
            print(f"\nFehler: {r_buch} wurde nicht gefunden!")
    else:
        print("\nDas Regal ist leer. Nichts zu entfernen!")


def menue():
    while True:
        m_auswahl = input("""
--- Virtuelles Bücherregal ---:
1.	Buch hinzufügen
2.	Buch entfernen
3.	Bücher anzeigen
4.	Buch suchen
5.	Beenden
Ihre Wahl: """)

        match m_auswahl:
            case "1":
                hinzufuegen()
            case "2":
                entfernen()
            case "3":
                anzeigen()
            case "4":
                suchen()
            case "5":
                break
            case "69":
                print("Döner")  #IStillLoveKebab
            case _:
                try:
                    int(m_auswahl)  #prüfen ob string als integer möglich ist, wenn ja dann richtige Zahl auffordern
                    print("\nUngültige Auswahl. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
                except ValueError:
                    print("\nBitte geben Sie eine gültige Zahl ein.")
        pass


menue()