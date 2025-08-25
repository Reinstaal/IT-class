# def fe(): a = int(input()); print((a*(a+1))/2)
# fe()
#
# def fe2(): a = int(input("Kleine Zahl\n")); b = int(input("Große Zahl\n")); print(((b*(b+1))/2)-((a*(a-1))/2))
# fe2()

def fe3():
    summe = 0
    a = int(input("Type a number:10\n"))
    for i in range(a+1):
        summe += i
    print(summe)

fe3()