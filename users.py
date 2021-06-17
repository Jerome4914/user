class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawl(self, amount):
        self.balance -= amount
        if amount > self.balance:
            self.balance -= 5
            print("Insufficient Funds Charging a $5 fee")  
        return self   
    def display_user_balance(self):
        self.balance
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:    
            self.balance = self.balance + self.balance * self.int_rate
        return self
Account1=BankAccount(.01, balance=0)
Account2=BankAccount(.01, 0)

class User:
    def __init__(self, name, email,):
        self.name = name
        self.email = email
        self.account = BankAccount(0.01)
    def make_withdrawal(self, ammount):
        self.account.withdrawl(ammount)
        return self
    def make_deposit(self, ammount):
        self.account.deposit(ammount)
        return self
    def display_user_balance(self):
        self.account.display_user_balance()
        return self
    def transfer_money(self, other_user, ammount):
        self.make_withdrawal(ammount)
        other_user.make_deposit(ammount)
guido=User("Guido Sapien", "guido@gmail.com",)
# Micah=User("Minecraft Micah", "minecraftmicah@hotmail.com", (500))
# Harlow=User("Princess Harlow", "princessharlow@yahoo.com",(0))
guido.make_deposit(100).make_deposit(800).make_deposit(100).make_withdrawal(500).make_deposit(1000).display_user_balance()
# Micah.make_deposit(80), Micah.make_deposit(80), Micah.make_withdrawal(50), Micah.make_withdrawal(50)
# Harlow.make_deposit(1500), Harlow.make_withdrawal(100), Harlow.make_withdrawal(100), Harlow.make_withdrawal(100)
# guido.transfer_money(Harlow, 50),
# print(f"User: {guido.name}, Balance: ${guido.account_ballance}, User: {Harlow.name}, Balance: ${Harlow.account_ballance}")
harry=User("Harry Potter", "voldilocks@hogwarts.com")

harry.make_deposit(100).make_withdrawal(20).display_user_balance()
# print(harry.account.yield_interest().display_user_balance())
guido.transfer_money(harry,50)
# print(harry.display_user_balance(), guido.display_user_balance())
harry.make_withdrawal(135).display_user_balance()
print(harry.display_user_balance())
