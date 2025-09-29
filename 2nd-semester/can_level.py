class Tank:
    def __init__(self, name, level, capacity):
        self.name = name
        self.level = level
        self.capacity = capacity

    def showInfo(self):
        return f"{self.name}, current Level: {self.level} out of {self.capacity}L"


def addTank():
    print("Please put in variables for naming, level and capacity for the can. Type 'Stop' any time to end and show all.")
    name = input("Insert tank name: ")
    level = input("Insert current level: ")
    capacity = input("Insert maximum capacity of tank: ")
    if "stop" in (name.lower(), level.lower(), capacity.lower()):
        return
    return tanks.append(Tank(name, level, capacity))

def printTanks():
    print("\n------------ ------------ ------------")
    for tank in tanks:
        print(tank.showInfo())
    print("------------ ------------ ------------\n")

def quitApp():
    print("Roger that, quitting! T(h)anks for using!")
    raise QuitApp

def menu():
    try:
        print("Welcome to your totally trusted can level app.")
        while True:
            menuChoice = input("Input and enter one of the following to continue, or press 'Enter' to close the app: \n"
            "1 - Add tank \n"
            "2 - Show tanks \n"
            "3 - Exit \n")
            match menuChoice:
                case "":
                    quitApp()
                case "3":
                    quitApp()
                case "1":
                    addTank()
                case "2":
                    printTanks()
                case _:
                    print("Unaccapted input.\n")
    except QuitApp:
        pass

class QuitApp(Exception):
    pass


tanks = []
menu()