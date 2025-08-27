def verify():
    verificationDigit = 0
    for i, digit in enumerate(barcode, 1):
        if i%2 == 0:
            verificationDigit += digit*3
        else:
            verificationDigit += digit
    return verificationDigit%10


barcode = [5,8,4,3,6,6,5,4,2,9]

print(verify())