class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f'{self.name}, Account Balance:', self.account_balance)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
christian = User("Christian", "christian@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(300)
guido.make_withdrawal(300)
guido.display_user_balance()

monty.make_deposit(50)
monty.make_deposit(150)
monty.make_withdrawal(50)
monty.make_withdrawal(149)
monty.display_user_balance()

christian.make_deposit(1000)
christian.make_withdrawal(200)
christian.make_withdrawal(200)
christian.make_withdrawal(200)
christian.display_user_balance()


