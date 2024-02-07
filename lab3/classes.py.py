1
class Aliyar():
    def get_String(self):
        self.str1=input()
    def print_String(self):
        print(self.str1.upper())
str1=Aliyar()
str1.get_String()
str1.print_String()

2
class Shape():
    def __init__(self):
            pass
    def area(self):
            print(0)
class Square(Shape):
    def __init__(self,length=0):
        Shape.__init__(self)
        self.length=length
    def area(self):
          self.length=int(input())
          print(self.length*self.length)

Asqr=Shape()
Square().area()
Asqr.area()

3
class Shape():
    def __init__(self):
            pass
    def area(self):
            return 0  
class Square(Shape):
    def __init__(self,length=0):
        Shape.__init__(self)
        self.length=length
    def area(self):
          return self.length*self.length

class Rectangle(Shape):
    def __init__(self):
         self.length=int(input())
         self.width=int(input())
    def area(self):
        return self.length*self.width
rect=Rectangle()
print(rect.area())
    
4
import math
class Point():
    def __init__(self):
        pass
    def show(self):
        self.x=int(input("x = "))
        self.y=int(input("y = "))
        print(f"Point({self.x},{self.y})")
    def move(self):
        self.a=int(input("a = "))
        self.b=int(input("b = "))
        print(f"New point({self.a},{self.b})")
    def dist(self):
        print(math.sqrt((self.x-self.a)**2+(self.y-self.b)**2))
G = Point()
G.show()
G.move()
G.dist()

5
class Account():
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
    def deposit(self):
        self.deposit=int(input())
        self.balance+=self.deposit
        print("Deposit accepted!")
    def withdrawal(self):
        self.wd=int(input())
        if self.balance>=self.wd:
            self.balance-=self.wd
            print("Withdrawal accepted!")
        else:
            print("Funds unavailable!")
bank = Account('Aliyar',1000)
print(bank)
bank.deposit()
bank.withdrawal()

6
import math
class filter():
    def __init__(self):
        pass
    def num(self):
        self.num=int(input())
        list+=self.num
        return self.num
    def fil(self):
        sum=0
        for i in range(1,9):
            if (self.num)/i==0:
                sum+=1
            if sum==2:
                list2.append(self.num)
        print(list2)
            
list1=[]
list2=[]
filter().fil()


