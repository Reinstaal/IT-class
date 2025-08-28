# Make 2d "array"(list) for function searchTopseller(criteria: int, searchValue: int): string

def searchTopseller(criteria, searchValue):
    wine = []
    maxSales = 0
    for i in sales:
        if i[criteria] == searchValue:
            if i[4] > maxSales:
                maxSales = i[4]
                wine = i
    return str(wine[0])+str(wine[1])+str(wine[2])+str(wine[3])


sales = [[123,456,78,9,46], [333,125,20,4,998], [123,125,78,4,70], [333,456,20,9,199]]

criteria =  int(input("""Tip and enter the criteria for the best-seller:
0. Region
1. Grape variety
2. Year
3. Taste
"""))
searchValue = int(input("Give a criteria number: "))
print(searchTopseller(criteria, searchValue))