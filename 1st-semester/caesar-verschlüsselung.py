def chiffre():
    klein = "abcdefghijklmnopqrstuvwxyza"
    gross = "ABCDEFGHIJKLMNOPQRSTUVWXYZA"
    verschluesselung = {}

    for i in range(26):
        verschluesselung[klein[i]] = klein[i+1]
        verschluesselung[gross[i]] = gross[i+1]
    return verschluesselung


def n_text(o_text):
    neuer_text = ""
    for buchstabe in o_text:
        if buchstabe in x:
            neuer_text = neuer_text + x[buchstabe]
        else:
            neuer_text = neuer_text + buchstabe
    return neuer_text


x = chiffre()
print(x)
def menu():
    while True:
        o_text = input("\nGeben Sie einen Text zum Verschlüsseln an: ")
        print(f"Der verschlüsselte Text:", n_text(o_text))

menu()