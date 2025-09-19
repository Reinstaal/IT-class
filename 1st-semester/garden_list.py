plants = []

def abrufen():
    with open('plants file.txt', 'r') as file:
        for i in file:
            plants.append(i.strip())
    print('Pflanzen aus Datei geladen')


def speichern():
    with open('plants file.txt', 'w') as file:
        for i in plants:
            file.write(i+'\n')
    print('Pflanzen in Datei gespeichert.')


def hinzufuegen():
    plant = input('Pflanze: ')
    plants.append(plant)


def anzeigen():
    if plants:
        for i in range(len(plants)):
            print(f"{i + 1}. {plants[i]}")
    else:
        print("Die Liste ist leer")

def entfernen():
    plant = input('Pflanzenname zum Entfernen: ')
    if plant in plants:
        plants.remove(plant)
    else: print(f'{plant} existiert nicht.')

def menu():
    while True:
        auswahl = input('''
Hauptmenü:
1. Pflanze hinzufügen
2. Pflanze entfernen
3. Pflanzen anzeigen

0. Beenden\n''')

        match auswahl:
            case '1':
                hinzufuegen()

            case '2':
                if not plants:
                    print("Die Liste ist leer")
                else:
                    print('Folgende Pflanzen können entfernt werden:\n'
                          '______________________________________________')
                    anzeigen()
                    entfernen()

            case "3":
                print('Folgende Pflanzen haben wir uns schon notiert:\n'
                      '______________________________________________')
                anzeigen()

            case "0":
                break

            case _:
                print("Ungültige Eingabe!")

        speichern()
abrufen()
menu()