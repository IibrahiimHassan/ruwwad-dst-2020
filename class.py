class BankAccount:
    def __init__(self):
        accountNumber=int(input("Enter the accounNumber:"))
        name=input("Enter the name:")
        balance=float(input("Enter the balance:"))
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance

    def Deposit(self,deposit):
        self.balance=self.balance+deposit
    
    def Withdrawal(self,withdrawal):
        if withdrawal>self.balance:
            print("insufficient fund")
        else:
            self.balance=self.balance-withdrawal
        

    def banFees(self,bankfees):
        self.balance=(self.balance) * (5/100)

    def display(self):
        print("The account details are:"+" "+" "+"accountNumber"+" "+str(self.accountNumber)+"name:"+self.name+" "+"balance:"+str(self.balance))

account1=BankAccount()

account1.display() 
Question=int(input("what do you want to do(1.Deposit 2.Withdrawal 3.Balance):"))
if Question==1:
    amount=int(input("Enter the amount:"))
    account1.Deposit(amount)
    account1.display()
    
elif Question==2:
    amount=int(input("Enter the amount:"))
    account1.Withdrawal(amount)
    account1.display()

elif Question==3:
    account1.display()

       
