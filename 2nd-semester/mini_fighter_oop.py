import math


class Fighter:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.hunger = 0

    def checkLoss(self):
        if (self.hp <= 0 or self.strength <= 0):
            return True
        return False

    def showStatus(self):
        return f"{self.name} | HP: {self.hp} | STR: {self.strength} |  Hunger: {self.hunger}"

    def action(self, enemy):
        while True:
            choice = input(f"It's {self.name} turn! Attack(A) or Eat(E): \n").strip().lower()
            if choice == "a" or choice == "e":
                attackMight = max(0, math.floor((self.strength-self.hunger)/2))
                if choice == "e":
                    self.hunger -= 2
                    if self.hunger < 1:
                        print(f"{self.name} hunger fully restored!")
                        self.hunger = 0
                    break
                if self.hunger == 10:
                    print(f"{self.name} is too hungry.. no action was taken.")
                    break
                if choice =="a":
                    enemy.hp -= attackMight
                    if attackMight <= 0:
                        print(f"Attack missed, {self.name} is too weak!")
                    else:
                        print(f"{self.name} hit {enemy.name} for {attackMight} damage!!")
                    self.hunger += 1
                break
            else:
                print("Illegal input! Try again.")


def combatStatus():
    print()
    print(red.showStatus())
    print(blue.showStatus())
    print()

def combat():
    while not (red.checkLoss() or blue.checkLoss()):
        combatStatus()
        red.action(blue)
        if blue.checkLoss() == True:
            print("Red wins!")
            break
        blue.action(red)
        if red.checkLoss() == True:
            print("Blue wins!")
            break


red = Fighter("Red", 50, 10)
blue = Fighter("Blue", 60, 9)
combat()