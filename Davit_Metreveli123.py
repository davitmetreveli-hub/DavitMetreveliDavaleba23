class Bank_Account:
    def __init__(self, account_name, balance=0):
        self.accountname = account_name
        self.balance = balance
    def getter(self):
        return self.__account_name
    def setter(self, name):
        self.accountname = name
    def deposit(self,
class Bankaccount:
    def __init__(self, accountname, balance=0):
        self.accountname = accountname
        self.balance = balance
    def getaccname(self):
        return self.__accountname
    def setaccname(self, name):
        self.__accountname = name
    def deposit(self, amount):
        self.__balance += amount
        print(f"sucessful deposit ow you have {self.balance}")
    def undeposit(self, amount):
        if amount <= self.balance:
            self.balance = balance - amount
            print(f"undeposit succesfuk now you have {self.__balance}")