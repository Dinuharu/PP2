class Bankaccount:
    def __init__(self):
        self.owner = input("Enter owner's name: ")
        self.balance = 0
        
    def deposit(self):
        self.deposited = int(input("Enter amount to deposit: "))
        self.balance += self.deposited
        print("Balance after deposit:", self.balance)
        
    def withdraw(self):
        self.withdrawed = int(input("Enter amount to withdraw: "))
        if self.withdrawed > self.balance:
            print("Not enough money")
        else:
            self.balance -= self.withdrawed
            print("Balance after withdrawal:", self.balance)

zxc = Bankaccount()
zxc.deposit()
zxc.withdraw()
