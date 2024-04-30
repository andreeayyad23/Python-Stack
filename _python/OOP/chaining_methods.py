class User:


    def __init__(self, username):
        self.name = username
        self.account_balance = 0


    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self


    def make_deposit(self, amount):
        self.account_balance += amount
        return self


    def display_user_balance(self):
        print(self.account_balance)

guido = User("Andree AYYAD")

guido.make_deposit(700).make_deposit(400).make_deposit(500).make_withdrawal(50).display_user_balance()