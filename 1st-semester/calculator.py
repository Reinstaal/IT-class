def addi():
    a = int(input("wert a : "))
    b = int(input("wert b : "))
    print(f'{a}+{b}= {a + b}')

def subbi():
    a = int(input("wert a : "))
    b = int(input("wert b : "))
    print(f'{a}-{b}= {a - b}')

def multi():
    a = int(input("wert a : "))
    b = int(input("wert b : "))
    print(f'{a}*{b}= {a * b}')

def divi():
    a = int(input("wert a : "))
    b = int(input("wert b : "))
    print(f'{a}/{b}= {a / b}')

while True:
    print ('''
1 - Addition
2 - Subtraktion
3 - Multiplikation
4 - Division
9 - Programm beenden''')
    op = int(input("Operation : "))

    match op:
        case 1:
            addi()
        case 2:
            subbi()
        case 3:
            multi()
        case 4:
            divi()
        case 5:
            addi()
            subbi()
            multi()
            divi()
        case 9:
            break
        case _:
            print(f"FEHLER!!!!!!! :c")