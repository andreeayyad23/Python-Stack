class BankAccount:

    def __init__(self, int_rate, balance=0):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance - amount > 0:
            self.balance - amount
        else:
            print("Insufficient funds: Charging a $5 fee")
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

account2.deposit(1500).deposit(2400).deposit(300).deposit(225210).yield_interest().display_account_info()