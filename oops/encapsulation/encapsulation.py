'''
class Laptop:
    def __init__(self,name,price):
        self.__name=name
        self.__price=price
    
    def getLaptopInfo(self):
        print(self.__name)
        print(self.__price)
    
    def setprice(self,price):
        self.__price=price

l1=Laptop("DELL",48000)
l1.getLaptopInfo()
l1.setprice(90000)
l1.getLaptopInfo()


class Employee:
    def __init__(self,name,empid,sal):
        self.__name=name
        self.__empid=empid
        self.__sal=sal
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
    def getempid(self):
        return self.__empid
    def setempid(self,empid):
        self.__empid=empid
    def getsal(self):
        return self.__sal
    def setsal(self,sal):
        self.__sal=sal

    def working(self):
        print("Employee is working as Engineer")
    def playing(self):
        print("Employee Plays Cricket")
    def learning(self):
        print("Employee is learning Python")

e1=Employee("AKSHITHA",123,70000)
print(e1.getname())
print(e1.getempid())
print(e1.getsal())
e1.working()
e1.playing()
e1.learning()

e1.setname("NANDHITHA")
print(e1.getname())
e1.setempid(124)
print(e1.getempid())
e1.setsal(20000)
print(e1.getsal())
e1.working()
e1.playing()
e1.learning()
'''
class Login:
    def __init__(self):
        self.__username="Kane"
        self.__password="Kane@123"
    def getUserName(self):
        return self.__username
    def getUserPassword(self):
        return self.__password
    def setUserName(self,un):
        self.__username=un
    def setUserPassword(self,pw):
        self.__password=pw
    def check_login(self,input_username,input_password):
        return (input_username==self.__username and input_password==self.__password)

l1=Login()
print("                  LOGIN PAGE                      ")
input_username=input("USERNAME:")
input_password=input("PASSWORD:")
if l1.check_login(input_username,input_password):
    print("LOGIN SUCCESSFUL")
else:
    print("INVALID CREDENTIALS")

#define an encapsulated class to verify the product price using data hiding

class Mobile:
    def __init__(self,name,color,price):
        self.__name=name
        self.__color=color
        self.__price=price
    def getname(self):
        return self.__name
    def getcolor(self):
        return self.__color
    def getprice(self):
        return self.__price
    def setname(self,name):
        self.__name=name
    def setcolor(self,color):
        self.__color=color
    def setprice(self,price):
        if price>30000:
            self.__price=price
        else:
            print("Minimum price is:",self.__price)
m1=Mobile("VIVO","PURPLE",20000)
print(m1.getname())
print(m1.getcolor())
print(m1.getprice())
print("--"*7)
m1.setprice(9000)
print(m1.getname())
print(m1.getcolor())
print("--"*7)
m1.setprice(99000)
print(m1.getname())
print(m1.getcolor())
print(m1.getprice())

class Bag:
    def __init__(self,color,price):
        self.__color=color
        self.__price=price
    def getcolor(self):
        return self.__color
    def getprice(self):
        return self.__price
    def setcolor(self,color):
        self.__color=color
    def setprice(self,price):
        self.__price=price
    def storing(self):
        print("Bag Stores Books,Tiffin Box,Bottle")
    def carrying(self):
        print("Bag Carries Keychain")
b1=Bag("Green",2500)
print(b1.getcolor())
print(b1.getprice())
b1.storing()
b1.carrying()
b1.setcolor("White")
b1.setprice(5000)
print(b1.getcolor())
print(b1.getprice())
b1.storing()
b1.carrying()