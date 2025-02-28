class Bankaccount:
    def __init__(self,accountname,balance=0):
        self.__accountname = accountname
        self.__balance = balance
    def getaccname(self):
        return self.__accountname
    def getbalance(self):
        return self.__balance
    def setaccountname(self,newaccountname):
        self.__accountname = newaccountname
    def setbalance(self,newbalance):
        self.__balance = newbalance
    def deposit(self,amount):
        self.__balance += amount
        print(f"თანხა შეტანილია ახლა თქვენ გაქვთ{self.__balance} ლარი")
    def withdraw(self, amount):
        self.__balance -= amount
        print(f"თანხა გამოტანილია თქვენ გაქვთ{self.balance} ლარი")
