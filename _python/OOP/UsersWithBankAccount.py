class User:
    def __init__(self, name):

        self.name = name
        self.account = BankAccount(int_rate=0.04, balance=0)
    
    def make_deposit(self, amount):

        self.account.balance += amount
        return self
    
    def make_withdrawl(self, amount):
        self.account.balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")
        return self
    
    def transfer_money(self, another_user, amount):

        self.account.balance -= amount
        another_user.account.balance += amount
        self.display_user_balance()
        another_user.display_user_balance()
        return self




class BankAccount:

    def __init__(self, int_rate = 0.03, balance=0):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self        

    def display_account_info(self):
        print("Balance: " + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0 :
            self.balance += self.balance * self.int_rate
        else:
            print("Balance is negative")
        return self        


account1 = BankAccount(0.01)
account2 = BankAccount(0.02, 100)

account1.deposit(1000).deposit(1050).deposit(50).withdrawal(10000).yield_interest().display_account_info()

account2.deposit(1500).deposit(2400).deposit(300).deposit(250).yield_interest().display_account_info()