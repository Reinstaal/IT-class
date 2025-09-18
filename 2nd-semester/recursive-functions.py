def sumRec(n):
    if n == 0:
        return 0
    return n + sumRec(n-1)

def calcFactorialRec(m):
    if m == 1:
        return m
    if m == 0:
        return 0
    return m * calcFactorialRec(m-1)

def firstTryCalcFactorialIterative(o):
    for i in range(o-1):
        i = i + 1
        o = i * o
    return o

def secondTryCalcFactorialIterative(p):
    for i in range(1,p):
        p = i * p
    return p

def fibonacciSequenceRec(q):
    if q == 0:
        return q
    if q == 1:
        return q
    if q > 1:
        return fibonacciSequenceRec(q-1) + fibonacciSequenceRec(q-2)

def fibonacciSequenceIterative(r):
    collectFibonacci = []
    if r == 0:
        return r
    if r == 1:
        return r
    a = 0
    b = 1
    for i in range(1,r):
        c = a + b
        a = b
        b = c
        collectFibonacci.append(a)
    collectFibonacci.append(c)
    return collectFibonacci

def printFullNumberSequenceRec(s):
    print(s)
    if s == 0:
        pass
    else:
        printFullNumberSequenceRec(s-1)
        print(s)

def printFullNumberSequenceIterative(t):
    for i in range(t):
        print(t-i)
    for i in range(t):
        print(i)
    return i+1


print(sumRec(4))
print(calcFactorialRec(4))
print(firstTryCalcFactorialIterative(4))
print(secondTryCalcFactorialIterative(4))
print(fibonacciSequenceRec(10))
print(fibonacciSequenceIterative(10))
printFullNumberSequenceRec(3)
print(printFullNumberSequenceIterative(3))