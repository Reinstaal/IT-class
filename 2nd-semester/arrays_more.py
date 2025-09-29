from array import array


# 1) output every 2nd element in an array with a function
def everySecondElement():
    for i, number in enumerate(exercise1, start=1):
        if i%2 == 0:
            print(number)


def everySecondElement2():
    collectList = []
    for i, number in enumerate(exercise1, start=1):
        if i%2 == 0:
            collectList.append(number)
    return collectList


exercise1 = array('i',[1,2,3,4,5,6,7,8,9,10,100,200,300,400,5555555,555555555])

print("\nexercise 1:")
everySecondElement()
# or as list:
print(everySecondElement2())


# 2) Write sum function for int array
def sumArray():
    sum = 0
    for i, number in enumerate(exercise2):
        sum += number
    return sum


exercise2 = array('i',[1,2,3,4,5,6,7,8,9,10,100,200,300,400])

print("\nexercise 2:")
print(sumArray())
# Check as 
print(sum(exercise2))


# 3) output if first element is lesser/greater/equal to last element
def sizeComparision(excersize3Array):
    if excersize3Array[0] > excersize3Array[-1]:
        return "Greater"
    elif excersize3Array[0] == excersize3Array[-1]:
        return "Equal"
    else:
        return "Less"


exercise3Less = array('i',[1,2,3,4,5,6,7,8,9,10,100,200,300,400])
exercise3Great = array('i',[1,2,3,4,5,6,7,8,9,10,100,200,300,0])
exercise3Equal = array('i',[400,2,3,4,5,6,7,8,9,10,100,200,300,400])

print("\nexercise 3:")
print(sizeComparision(exercise3Less))
print(sizeComparision(exercise3Great))
print(sizeComparision(exercise3Equal))


# 4) Create a function that takes two numbers as arguments and 
# returns an array containing the multiples of the first number, 
# with as many multiples as specified by the second number.
def multiplyItselfByAmountSecondNumber(firstNumber, secondNumber):
    exercise4Calculate = []
    firstNumberCalculate = 0
    for i in range(secondNumber):
        firstNumberCalculate += firstNumber
        exercise4Calculate.append(firstNumberCalculate)
    return exercise4Calculate

print("\nexercise 4:")
print(multiplyItselfByAmountSecondNumber(7, 5))
print(multiplyItselfByAmountSecondNumber(12, 10))
print(multiplyItselfByAmountSecondNumber(17, 6))


# 5) Create a function that takes an array containing at least two numbers 
# and returns the second largest number in the array.
def secondLargestNumber(exercise5):
    exercise5List = []
    for i, number in enumerate(exercise5):
        exercise5List.append(number)
    # also works with python arrays as they are dynamic wrappers: could use NumPy arrays instead
    exercise5List.sort()
    # exercise5List = sorted(exercise5List)
    return exercise5List[-2]
    

exercise5FirstArray = array('i', [10, 40, 30, 20, 50])
exercise5SecondArray = array('i', [25, 143, 89, 13, 105])
exercise5ThirdArray = array('i', [54, 23, 11, 17, 10])

print("\nexercise 5:")
print(secondLargestNumber(exercise5FirstArray))
print(secondLargestNumber(exercise5SecondArray))
print(secondLargestNumber(exercise5ThirdArray))