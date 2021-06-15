class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_ballance = 0
    def make_withdrawal(self, ammount):
        self.account_ballance -= ammount
        return self
    def make_deposit(self, ammount):
        self.account_ballance += ammount
        return self
    def display_user_balance(self):
        self.account_ballance
        return self
    def transfer_money(self, other_user, ammount):
        self.make_withdrawal(ammount)
        other_user.make_deposit(ammount)
guido=User("Guido Sapien", "guido@gmail.com")
Micah=User("Minecraft Micah", "minecraftmicah@hotmail.com")
Harlow=User("Princess Harlow", "princessharlow@yahoo.com")
guido.make_deposit(100).make_deposit(800).make_deposit(100).make_withdrawal(500).make_deposit(1000).display_user_balance()
# Micah.make_deposit(80), Micah.make_deposit(80), Micah.make_withdrawal(50), Micah.make_withdrawal(50)
# Harlow.make_deposit(1500), Harlow.make_withdrawal(100), Harlow.make_withdrawal(100), Harlow.make_withdrawal(100)
# guido.transfer_money(Harlow, 50),
print(f"User: {guido.name}, Balance: ${guido.account_ballance}, User: {Harlow.name}, Balance: ${Harlow.account_ballance}")