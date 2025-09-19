def inputTerms():
    print("Put in terms with enter. Leaving the input empty and pressing enter will sort your terms.\n")
    while True:
        inputTermUser = input("Term: ")
        if inputTermUser == "":
            break
        if inputTermUser in list:
            print("This term has already been added. Please add a different term.")
            continue
        list.append(inputTermUser)

def sortedPrint(list):
    print("\n---Sorted output---")
    sortedList = sorted(list)
    for i, term in enumerate(sortedList, 1):
        print(f"{i}: " + term)

def main():
    print("Welcome at taal performance control: Sort terms. Shirley the best service around!")
    while True:
        inputTerms()
        if list == []:
            print("No terms added to list. The Program will now terminate for your safety.")
            break
        sortedPrint(list)
        break


list = []

main()