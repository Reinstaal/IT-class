class Ape:
    name = None
    age = None
    sex = None
    listOfAllNames = []

    def showInfo(self):
        return f"Name: {self.name} | Age: {self.age} | Sex: {self.sex}"

    def setName(self, newName):
        self.name = newName

        
ape1 = Ape()
ape1.name = "Chita"
ape1.age = 5
ape1.sex = "M"

ape2 = Ape()
ape2.name = "Mandela"
ape2.age = 10
ape2.sex = "M"


print(ape1.showInfo())
print(ape2.showInfo())

newName = input('Enter new name: ')
ape1.setName(newName)
print(ape1.showInfo())
