class BankAccount:
    def __init__(self,name,balance=0):
        if balance<0:
            raise ValueError("value cannot be negative")
        self.name=name
        self.balance=balance
        
    def deposite(self,amount):
        if amount<0:
            raise ValueError("amount can not be negative")
        self.balance+=amount
        return self.balance
    
    def withdrawal(self,amount):
        if amount<0:
            raise ValueError("withdraw must be positive")
        if amount>self.balance:
            raise ValueError("Insuficient balance")
        self.balance-=amount
        return self.balance
    
    def get_balance(self):
        return self.balance
        