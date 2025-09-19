def checkPrime(p):
    for i in range(2,p-1):
        if p%i == 0:
            return False
    return True

def checkPrimeSkipRoundNumbers(q):
    if q == 2:
        return True
    checkingPrime = q%2
    if checkingPrime == 0:
        return False
    for i in range(3,q-1,2):
        checkingPrime = q%i
        if checkingPrime == 0:
            return False
    return True

def checkPrimeRec(r):
    if r == 1:
        return False
    return isPrime(r, r-1)

def isPrime(t, u):
    if u == 1:
        return True
    if t%u == 0:
        return False
    return isPrime(t, u-1)
    

wholeNumberToBeChecked = int(input("Enter whole number: "))
primeCheck = checkPrime(wholeNumberToBeChecked)
if primeCheck:
    print(f"{wholeNumberToBeChecked} is a prime number!")
else:
    print(f"{wholeNumberToBeChecked} is not a prime number :C")

primeCheck = checkPrimeSkipRoundNumbers(wholeNumberToBeChecked)
if primeCheck:
    print(f"{wholeNumberToBeChecked} is a prime number!")
else:
    print(f"{wholeNumberToBeChecked} is not a prime number :C")

primeCheck = checkPrimeRec(wholeNumberToBeChecked)
if primeCheck:
    print(f"{wholeNumberToBeChecked} is a prime number!")
else:
    print(f"{wholeNumberToBeChecked} is not a prime number :C")