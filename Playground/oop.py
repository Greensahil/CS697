#Procedural vs object oriented
import math

class Circle:
   
    #a method without self is a utlity function
    def __init__(self,radius = 10,color = 'black'): #like constructor in java which is invoke when object is created from a class
        self.radius = radius
        self.color = 'black'
    
    def getArea(self):
        return math.pi * self.radius * self.radius

c1=Circle()
print(c1.radius)

c2 = Circle(radius=15)
print(c2.radius)
    
print(c1.getArea())



class Account:
    numAccounts = 0
    def __init__(self, *locations):
        self.balance = balance
        Account.numAccounts +=1   #saying account because we want this to be shared between all instances of the class
    

    def deposite(self, depositeAmount):
        if(depositeAmount < 0):
            print("cannot deposite negative ammount")
            return
        if(self.balance + depositeAmount >= 0):
            self.balance = self.balance + depositeAmount
        else:
            print("Cannot perform deposite")
        
    def withdraw(self, withdrawAmount):
        if(withdrawAmount < 0):
            print("cannot withdraw negative ammount")
            return

        if(self.balance - withdrawAmount >= 0):
            self.balance = self.balance - withdrawAmount
        else:
            print("Cannot perform deposite")
    
    def __str__(self):
        return f'Account balance {self.balance}'

a1 = Account()
a1.deposite(5)

print(a1)