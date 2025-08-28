from array import array

def verifyOld(barcode):
    verificationDigit = 0
    for i, digit in enumerate(barcode, 1):
        if i%2 == 0:
            verificationDigit += digit*3
        else:
            verificationDigit += digit
    return verificationDigit%10

def verify(barcode):
    verificationDigitTimes1 = sum(barcode[::2])
    verificationDigitTimes3 = sum(barcode[1::2])*3
    return (verificationDigitTimes1 + verificationDigitTimes3)%10


barcode1 = [5,8,4,3,6,6,5,4,2]
barcode2 = [4,3,2,1,9,8,7,7,7]
barcode3 = [9,8,7,6,5,4,3,2,1]

print(verifyOld(barcode1))
print(verifyOld(barcode2))
print(verifyOld(barcode3))
print(verify(barcode1))
print(verify(barcode2))
print(verify(barcode3))