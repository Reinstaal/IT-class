def checkPrime(p):
    for i in range(2,p-1):
        checkingPrime = p%i
        if checkingPrime == 0:
            return False
    return True

def checkPrimeSkipRoundNumbers(p):
    if p == 2:
        return True
    checkingPrime = p%2
    if checkingPrime == 0:
        return False
    for i in range(3,p-1,2):
        checkingPrime = p%i
        if checkingPrime == 0:
            return False
    return True


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