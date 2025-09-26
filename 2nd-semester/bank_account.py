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

    def deposit(self, value, date):
        self.__balance += value
        self.date = date
        print(f"Deposited {value}€ onto account")


    def withdraw(self):
        pass

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
tkto.deposit(22, "26.09.2025")
print(tkto.getBalance())

tskto = SavingsAccount()
tskto.deposit(44, "123.23.23")
print(tskto.getBalance())