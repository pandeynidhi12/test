#23 write a program to create a ATM ACCOUNT.
from abc import abstractmethod
import random
class ATM:
    @abstractmethod
    def CreateAccount(self):
        pass

    @abstractmethod
    def DepositeAmount(self,bal):
        pass

    @abstractmethod
    def withdrawAmount(self,amount):
        pass

    @abstractmethod
    def checkbal(self):
        pass

    @abstractmethod
    def  exit(self):
        pass

class Bank(ATM):
    balance=0
    def  __init__(self,a,b,c):
        self.name=a
        self.AadharNo=b
        self.branch=c
        self.AccountNo = random.randint(100000,999999)
    def  CreateAccount(self):
        print("emp name is",self.name)
        print("emp AadharNo. is", self.AadharNo)
        print("emp branch name is", self.branch)
        print("emp AccountNo.  is", self.AccountNo)
    def  DepositAmount(self,bal):
        self.balance=self.balance+bal
    def withdrawAmount(self,amount):
        self.balance=self.balance-amount
    def checkbal(self):
        print(self.balance)
    def exit(self):
        pass
name=input("enter the name")
AadharNo=int(input("enter the AadharNo "))
branch=input("enter the branch name")

k=Bank(name,AadharNo,branch)

while True:
    print("1.CREATE ACCOUNT")
    print("2.DEPOSITE")
    print("3.WITHDRAW")
    print("4.CHECKBAL")
    print("5.exit")
    x=int(input("enter the choice"))
    if(x==1):
        k.CreateAccount()
    elif(x==2):
        b=int(input("enter the deposit amount"))
        k.DepositeAmount(b)
    elif(x==3):
        b2=int(input("enter the withdraw amount"))
        k.withdrawAmount(b2)
    elif(x==4):
        k.checkbal()
    elif(x==5):
        break

