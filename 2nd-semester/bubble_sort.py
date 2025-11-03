def bubbleSort(unsortedArray):
    toBeSorted = unsortedArray.copy()
    changed = True
    while changed == True:
        changed = False
        for j in range(len(toBeSorted)-1):
            if toBeSorted[j] > toBeSorted[j+1]:
                saveElement = toBeSorted[j]
                toBeSorted[j] = toBeSorted[j+1]
                toBeSorted[j+1] = saveElement
                changed = True
    sortedArray = toBeSorted
    return sortedArray

def checkSorted():
    array =  [9999999999999995,33,12,4,22,1,39,3,63,21,21,81,74,15,19,0,18,8,71,59,41,245,573,63,9,123]
    sortedArray = sorted(array)
    bubbleSorted = bubbleSort(array)
    print("Unsorted Array:", array)
    print("Built-in sorted:", sortedArray)
    print("Bubble sorted", bubbleSorted)
    print("Check if same arrays: ", sortedArray == bubbleSorted)

checkSorted()