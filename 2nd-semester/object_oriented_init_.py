class Ape:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    # getter / setter
    def getName(self):
        return self.name
    
    def setName(self, value):
        self.name = value
    
    def getAlter(self):
        return self.age
    
    def setAge(self, value):
        if 0 <= int(value) < 99:
            self.age = value
        else:
            print("Unaccepted age, setting age to 0")
            self.age = 0
    
    def getSex(self):
        return self.sex

    def setSex(self, value):
        if str(value).lower() in ["male", "female", "diverse"]:
            self.sex = str(value).lower()
        else:
            print("Sex unknown, setting sex to unknown")
            self.sex = "unknown"
    
    def showInfo(self):
        return f"Name: {self.name} | Age: {self.age} | Sex: {self.sex}"


# Testing:
ape1 = Ape("Susi", 5, "female")
ape2 = Ape("Klaus", 8, "male")

print("Before any changes:")
print(ape1.showInfo())
print(ape2.showInfo())

# Changes:
ape1.name = "Lena"
ape2.age = 20

# Changes through setter
ape1.setAge(15)
ape1.setSex("MalE")
ape2.setSex("nani")

print("\nAfter changes:")
print(ape1.showInfo())
print(ape2.showInfo())

print("\nUsing a list:")
ape_list = []
ape_list.append(Ape("Mika", 2, "diverse"))
ape_list.append(Ape("Balu", 7, "male"))
ape_list.append(Ape("Nala", 5, "female"))

for ape in ape_list:
    print(ape.showInfo())