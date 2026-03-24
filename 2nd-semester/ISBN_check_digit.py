correctIsbn = [9, 7, 8, 3, 1, 4, 2, 3, 5, 0, 8, 4, 4]
wrongIsbn = [9, 7, 8, 3, 1, 4, 2, 3, 5, 0, 8, 4, 8]

def checkDigit(isbn):
    checkSum = 0
    for i in range(12):
        if i%2 == 0:
            checkSum = checkSum + isbn[i] * 1
        else:
            checkSum = checkSum + isbn[i] * 3

    tempCheckSum = checkSum - checkSum % 10 + 10
    checkSum = tempCheckSum - checkSum
    if isbn[12] == checkSum:
       return "Check digit is correct"
    return "ISBN is not up to standard! D: so spooky, who would do such a thing??"

print(checkDigit(correctIsbn))
print(checkDigit(wrongIsbn))