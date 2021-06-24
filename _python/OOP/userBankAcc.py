class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.bankAccount


    def deposit(self, amount):
        self.bankAccount.deposit(amount)
        return self


class BankAccount:
    def __init__(self, int_rate = 0.01 , balance = 0):
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        return self


    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = (self.balance - amount) - 5
        return self


    def display_account_info(self):
        print('Balance:$', self.balance)
        return self


    def yield_interest(self):
        self.balance = self.balance - (self.int_rate * self.balance)
        return self


Guido = BankAccount()
Christian = BankAccount()

Guido.deposit(100).deposit(200).deposit(300).withdraw(601).yield_interest().display_account_info()
Christian.deposit(500).deposit(500).withdraw(250).withdraw(250).withdraw(250).withdraw(300).yield_interest().display_account_info()