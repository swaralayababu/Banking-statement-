class BankAccount():
    def __init__(self):
        self.amount = 0
    def login(self,Account_No):
        self.Account_No = Account_No
        print("Welcome to ABC Banking System ")
    def deposit(self,Amount):
        self.amount += Amount
        print("Amount succesfully deposited")
    def withdraw(self,Amount):
        if(self.amount - Amount >= 500):
            self.amount -= Amount
            print("Amount successfully withdrawn")
        else:
            print("insufficient balance. You must have atleast Rs.500")
    def balance(self):
        print("your bank balance is:", self.amount)

a = BankAccount()
for i in range(0,30):
    print("1.Deposit 2.Withdraw 3.Check Balance 4.Exit")
    choice = int(input("Enter your choice:"))
    if (choice == 1):
        Amount = float(input("Enter the amount to be deposited:"))
        a.deposit(Amount)
    elif(choice == 2):
        Amount = float(input("Enter the amount to be withdrawn:"))
        a.withdraw(Amount)
    elif(choice == 3):
        a.balance()
    else:
        exit()
