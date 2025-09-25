class Tank:
    def __init__(self, name, level, capacity):
        self.name = name
        self.level = level
        self.capacity = capacity

    def showInfo(self):
        return f"Tank: {self.name}, current Level: {self.level} out of {self.capacity}L"


tanks = []

while True:
    print("Please put in variables for naming, level and capacity for the can. Type 'Stop' to end and show all.")
    name = input("Insert tank name: ")
    level = input("Insert current level: ")
    capacity = input("Insert maximum capacity of tank: ")
    if "stop" in (name.lower(), level.lower(), capacity.lower()):
        break
    tanks.append(Tank(name, level, capacity))

for tank in tanks:
    print(tank.showInfo())