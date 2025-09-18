'''
class Sample():
    def __init__(self):
        print("No argument constructor")
s1=Sample()
s1.__init__()

class Book:
    def __init__(self,name,price):
        self.name=name
        self.price=price

b=Book("Python",1999)
print(b.name)
print(b.price)
print("--"*10)
b1=Book("Java",1999)
print(b1.name)
print(b1.price)
print("--"*10)
b2=Book("SQL",999)
print(b2.name)
print(b2.price)
print("--"*10)
b3=Book("Django",9999)
print(b3.name)
print(b3.price)

class Student:
    def __init__(self,name,id):
        self.name=name #instance variable
        self.id=id
    def getStdInfo(self): #instance function
        print(self.name,self.id)
b=Student("Kane","Kane@123")
b.getStdInfo()
print("--"*10)
b1=Student("Jinny","Jinny@123")
b1.getStdInfo()

class Student:

    SchoolName="PySpiders"
    def __init__(self,name,r_no):
        self.name=name
        self.r_no=r_no
    def getStudentInfo(self):
        print(self.name+" "+self.r_no)
    @classmethod
    def getSchoolInfo(cls):
        print(Student.SchoolName)
    @staticmethod
    def feedBack():
        print("Very Easy Subjects")

s=Student("Ahi","A24")
s.getSchoolInfo()
s.getStudentInfo()
s.feedBack()    


class Employee:
    CompanyName="GOOGLE" #static variable
    def __init__(self,name,emp_id): #local variables
        self.name=name #instance varibles
        self.emp_id=emp_id
    def getEmployeeInfo(self): #instance method
        print(self.name)
        print(self.emp_id)
    @classmethod
    def getCompanyName(cls): 
        print(Employee.CompanyName)
    @staticmethod
    def getCompanyRating():
        print("5*")
e=Employee("Akshitha",1234) # 1st object creation
e.getEmployeeInfo()
e.getCompanyName()
e.getCompanyRating()
print("--"*10)
e1=Employee("Nandhitha",2341) # 2nd object creation
e1.getEmployeeInfo()
e1.getCompanyName()
e1.getCompanyRating()

'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getpersoninfo(self):
        print("Name:",self.name)
        print("Age:",self.age)
p=Person("Kane",21)
p.getpersoninfo()
p1=Person("Jinny",22)
p1.getpersoninfo()

class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def getcardetails(self):
        print("Brand:",self.brand)
        print("Color:",self.color)
    def set_color(self,color):
        self.color=color
c=Car("BMW","Black")
c.getcardetails()
c.set_color("Blue")
c.getcardetails()