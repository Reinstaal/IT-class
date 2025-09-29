# exercise:
# Build an own stack with:
# push(element): void
# pop(): element
# top(): element
# So I fucked up, with using parameters:

def push(stack, userInput):
    stack += userInput

def top(stack):
    stackIsEmpty = checkEmptyList(stack)
    if stackIsEmpty == 1:
        return
    else:
        lastIndexElement = len(stack) -1
        print(stack[lastIndexElement])

def pop(stack):
    stackIsEmpty = checkEmptyList(stack)
    if stackIsEmpty == 1:
        return
    lastIndexElement = len(stack) -1
    getElement = stack[lastIndexElement]
    stack.reverse()
    stack.remove(getElement)
    stack.reverse()

def checkEmptyList(stack):
    if stack == []:
        print("The list is empty.")
        true = 1
        return true
    else:
        false = 0
        return false

def menu(stack):
    userInput = input("Add an element:  ")
    push(stack, userInput)
    top(stack)
    pop(stack)
    top(stack)


stack = []
menu(stack)