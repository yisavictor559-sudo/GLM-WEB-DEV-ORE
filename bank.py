class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Let's test it out!
my_account = BankAccount("Oreoluwa", 100)
print(my_account.deposit(50))
print(my_account.withdraw(30))
print(my_account.withdraw(500)) 