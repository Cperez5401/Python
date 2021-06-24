class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f'{self.name}, Account Balance:', self.account_balance)
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
christian = User("Christian", "christian@python.com")

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(300).display_user_balance()

monty.make_deposit(50).make_deposit(150).make_withdrawal(50).make_withdrawal(149).display_user_balance()

christian.make_deposit(1000).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200).display_user_balance()