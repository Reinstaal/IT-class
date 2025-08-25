def ungueltig():
    print("Ungültige Eingabe, bitte eine Zahl oder 'Stop' zum Beenden): ")

zaehler = {}

while True:
        try:
            eingabe = input("Punkte der Runde eingeben (oder 'Stop' zum Beenden): ")
            if eingabe == "" and zaehler == 0:
                print("Es wurden keine Runden eingegeben.") #bei stop
                break
            elif eingabe.lower() == "stop":
                print("programm wird beendet: eingabe := 'stop'")
                print("Alle eingegebenen Punkte: ")
                for x in zaehler:
                    print(f"Runde {x+1}: {zaehler[x]}")

                print(f"\nSumme aller Runden: {sum(zaehler.values())}")
                print(f"\nHöchste Rundenpunktzahl: {max(zaehler.values())}")
                print(f"\nDurchschnittliche Rundenpunktzahl: {float(sum(zaehler.values())/float(x+1))}")

                eingabe_g = input("Grenzwert eingeben: ")
                try:
                    n = 0
                    for x in enumerate(zaehler):
                        if x > zaehler.values():
                            n = n+1
                        else:
                            pass
                    print(f"Alle Male über dem Grenzwert: {n}")
                except ValueError:
                    ungueltig()
                break
            elif int(eingabe) <0:
                print("Bitte nur positive Zahlen eingeben.")
            elif int(eingabe) > 180:
                print("Mehr als 180 Punkte pro Runde klingt aber stark nach Schummeln!")
            elif 0 <= int(eingabe) <= 180:
                zaehler[len(zaehler)] = int(eingabe)
                print(zaehler)
            else:
                ungueltig()
                print("else")
        except ValueError:
            if eingabe =="":
                print("Es wurden keine Runden eingegeben.")
                break
            ungueltig()
            print("except")