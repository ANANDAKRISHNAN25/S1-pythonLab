class BankAccount:
    def __init__(self):
        self.number=int(input("Enter the account number:"))
        self.name=input("Enter your name:")
        self.actype=input("Enter the account type s/c:")
        self.balance=0
        
    def withdraw(self):
        amount=int(input("Entert the amount to withdraw:"))
        if amount >= self.balance:
            print("Low Balance")
        else:
            self.balance= self.balance-amount
            print("Net balance is =",self.balance)
    def deposit(self):
        amount=int(input("Enter the amount to deposit:"))
        self.balance = self.balance+amount
        print("net balance :",self.balance)
        
    def display(self):
        print("net balance",self.balance)
        
obj= BankAccount()
while(True):
    print("\n1.Deposit Money \n2.Withdraw Money \n3.Exit")
    ch=int(input("Enteer the choice :"))
    if(ch==1):
        obj.deposit()
        
    elif(ch==2):
        obj.withdraw()
        
    else:
        exit(0)
obj.display()        
    


        
        
        
        
        
                    
            
        