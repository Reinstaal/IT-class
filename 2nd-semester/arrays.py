#Dokumentation für Arrays in python: https://docs.python.org/3/library/array.html
#signed: Vorzeichen (- und +)
#unsigned: Nur positive Zahlen

from array import array


testarray = array("I", [0,0,0,44])

#Verändern nach Index:
testarray[0] = 7

#Fehler: Funktioniert nicht, da Anzahl an Elementen festgesetzt sind bei Erstellung von Arrays
#testarray[5] = 8

#Jedoch ists bei Python möglich: 
#testarray.append(5)

#Mehrere gleichzeitig:
#testarray.extend([5,4,3])

for i in range(len(testarray)):
    print(testarray[i])
exit