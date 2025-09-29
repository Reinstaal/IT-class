# exercise: create class Customer
# customer is able to create bank acc
# difference in bank acc: checking and savings
# checking: add empty overdraft method
# savings: override deposit method

class Customer:
    def __init__(self, name, adresse, date):
        self.name = str(name)
        self.adresse = str(adresse)
        self.date = str(date)

class Account:
    def __init__(self):
        self.__balance = float(0)        
        self.haveInterest = float(0)
        self.customerID = str()
        self.owner = Customer
        self.__accMovement = []

    def deposit(self, value, date):
        if value > 0 and isinstance(value, int | float):
            self.__balance += value
            self.date = date
            self.__accMovement.append({"deposit": value, "date": date})
            print(f"Deposited {value}€ onto account")
            print(self.__accMovement)
        else:
            print("Not a positive value")

    def withdraw(self, value, date):
        if value > 0 and isinstance(value, int | float):
            self.__balance -= value
            self.date = date
            self.__accMovement.append({"withdraw": value, "date": date})
            print(f"Withdrawn {value}€ from account")
            print(self.__accMovement)
        else:
            print("Not a positive value")

    def interestCredit(self):
        pass

    def getBalance(self):
        return self.__balance

class CheckingAccount(Account):
    def __init__(self):
        super().__init__()

    def overdraft(self):
        pass

class SavingsAccount(Account):
    def __init__(self):
        super().__init__()

    def deposit(self, value, date):
        self._Account__balance += value
        self.date = date
        print(f"Deposited {value}€ onto savings account")


tkto = CheckingAccount()
tkto.deposit(23, "26.09.2025")
print(tkto.getBalance())
tkto.deposit(23.5, "27.09.2025")
tkto.withdraw(24, "28.09.2025")
print(tkto.getBalance())

tskto = SavingsAccount()
tskto.deposit(44, "123.23.23")
print(tskto.getBalance())