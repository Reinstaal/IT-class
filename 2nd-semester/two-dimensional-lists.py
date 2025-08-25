array = [[3,5,5,2,3,6],
         [43,435,55,2,443,78,7],
         [3798,3,3376,77,22,566912,8],
         [24,4,4,4,46,8,1148],
         [345,77,34,4,27,8,856,643,33,3,6,88]]

arraySum = []
arrayAllSum = []

for i in range(len(array)):
    arraySum = [sum(array[i])]
    for i in range(len(arraySum)):
        arrayAllSum = arrayAllSum + arraySum
        #arrayAllSum += arraySum

print(arrayAllSum)
exit