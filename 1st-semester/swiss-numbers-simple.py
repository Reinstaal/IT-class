wörterbuch = {
    0:  "Noll",
    1:  "Ett",
    2:  "Tva",
    3:  "Tre",
    4:  "Fyra",
    5:  "Fem",
    6:  "Sex",
    7:  "Sju",
    8:  "Atta",
    9:  "Nio",
    10: "Tio",
    11: "Elva",
    12: "Tolv",
    13: "Tretton",
    14: "Fjorton",
    15: "Femton",
    16: "Sexton",
    17: "Sjutton",
    18: "Aderton",
    19: "Nitton",
    20: "Tjugo",
    30: "Trettio",
    40: "Fyrtio",
    50: "Femtio",
    60: "Sextio",
    70: "Sjuttio",
    80: "Attio",
    90: "Nittio",
    100:    "Hundra"

}

while True:
    eingabe = int(input("Schwedische Zahl:\n"))
    try:
        print(eingabe, f"=", wörterbuch[eingabe])
    except:
        print("Ungültige Eingabe, Programm wird beendet")
        break


# for i in wörterbuch:
#     print(wörterbuch[i])