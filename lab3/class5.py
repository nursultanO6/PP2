class Account:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    def show_balance(self):
        print(self.balance)
        print(self.name)
    def deposit(self, mtd):
        self.balance += mtd
    def withdraw(self, withd):
        if(self.balance >= withd):
            self.balance -= withd 
        else:
            print("Error")     
p3 = Account("Nur", 0)
p3.deposit(150)
p3.show_balance()
p3.withdraw(120)
p3.show_balance()
p3.withdraw(40)