from array import array


# 1) output every 2nd element in an array with a function
def everySecondElement():
    for i, number in enumerate(excercise1, start=1):
        if i%2 == 0:
            print(number)


def everySecondElement2():
    collectList = []
    for i, number in enumerate(excercise1, start=1):
        if i%2 == 0:
            collectList.append(number)
    return collectList


excercise1 = array('i',[1,2,3,4,5,6,7,8,9,10,100,200,300,400,5555555,555555555])

print("\nExcercise 1:")
everySecondElement()
# or as list:
print(everySecondElement2())


# 2) Write sum function for int array
def sumArray():
    sum = 0
    for i, number in enumerate(excercise2):
        sum += number
    return sum


excercise2 = array('i',[1,2,3,4,5,6,7,8,9,10,100,200,300,400])

print("\nExcercise 2:")
print(sumArray())
# Check as 
print(sum(excercise2))


# 3) output if first element is lesser/greater/equal to last element
def sizeComparision(excersize3Array):
    if excersize3Array[0] > excersize3Array[-1]:
        return "Greater"
    elif excersize3Array[0] == excersize3Array[-1]:
        return "Equal"
    else:
        return "Less"


excercise3Less = array('i',[1,2,3,4,5,6,7,8,9,10,100,200,300,400])
excercise3Great = array('i',[1,2,3,4,5,6,7,8,9,10,100,200,300,0])
excercise3Equal = array('i',[400,2,3,4,5,6,7,8,9,10,100,200,300,400])

print("\nExcercise 3:")
print(sizeComparision(excercise3Less))
print(sizeComparision(excercise3Great))
print(sizeComparision(excercise3Equal))


# 4) Create a function that takes two numbers as arguments and 
# returns an array containing the multiples of the first number, 
# with as many multiples as specified by the second number.
def multiplyItselfByAmountSecondNumber(firstNumber, secondNumber):
    excercise4Calculate = []
    firstNumberCalculate = 0
    for i in range(secondNumber):
        firstNumberCalculate += firstNumber
        excercise4Calculate.append(firstNumberCalculate)
    return excercise4Calculate

print("\nExcercise 4:")
print(multiplyItselfByAmountSecondNumber(7, 5))
print(multiplyItselfByAmountSecondNumber(12, 10))
print(multiplyItselfByAmountSecondNumber(17, 6))


# 5) Create a function that takes an array containing at least two numbers 
# and returns the second largest number in the array.
def secondLargestNumber(excercise5):
    excercise5List = []
    for i, number in enumerate(excercise5):
        excercise5List.append(number)
    # also works with python arrays as they are dynamic wrappers: could use NumPy arrays instead
    excercise5List.sort()
    # excercise5List = sorted(excercise5List)
    return excercise5List[-2]
    

excercise5FirstArray = array('i', [10, 40, 30, 20, 50])
excercise5SecondArray = array('i', [25, 143, 89, 13, 105])
excercise5ThirdArray = array('i', [54, 23, 11, 17, 10])

print("\nExcercise 5:")
print(secondLargestNumber(excercise5FirstArray))
print(secondLargestNumber(excercise5SecondArray))
print(secondLargestNumber(excercise5ThirdArray))