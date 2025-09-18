class Bag:
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color
    def getbaginfo(self):
        print(self.name)
        print(self.price)
        print(self.color)
    def insertbook(self):      
        print("Inserted book into bag")
    def insertlaptop(self):
        print("Stored laptop into bag")


class Book:
    def __init__(self,name,no_of_pages,price):
        self.name=name
        self.no_of_pages=no_of_pages
        self.price=price
    def getbookinfo(self):
        print(self.name , self.no_of_pages, self.price)
    
class Laptop:
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color
    def getlaptopinfo(self):
        print(self.name,self.price,self.color)

class Student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
        self.bag=None
    def getstudentinfo(self):
        print(self.name,self.id,self.age)
    def goingtoschool(self):
        self.bag=Bag("Barbie",1500,"pink")
        self.bag.getbaginfo()
        print("Student is going to school")
    def booklap(self,b,l):
        b.getbookinfo()
        l.getlaptopinfo()
    def insertion(self):
        self.bag.insertbook()
        self.bag.insertlaptop()

s1=Student("Akshu",1,12)
print("Student Details")
s1.getstudentinfo()
s1.goingtoschool()
s1.booklap(Book("Eng",300,"150rs"),Laptop("Dell",80000,"Black"))
s1.insertion()
