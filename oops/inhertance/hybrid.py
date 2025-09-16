'''
class A:
    def a(self):
        print("class A")
class B:
    def b(self):
        print("class B")
class C(A,B):
    def c(self):
        print("class C")
class D(C):
    def d(self):
        print("class D")
class E(D):
    def e(self):
        print("class E")
class F(D):
    def f(self):
        print("class F")


h=E()
h.a()
h.b()
h.c()
h.d()
h.e()
h1=F()
h1.a()
h1.b()
h1.c()
h1.d()
h1.f()


class Vehicle:
    def __init__(self,brand,wheels):
        self.brand=brand
        self.wheels=wheels
    def getVehicleInfo(self):
        print("Brand name is:",self.brand)
        print("no of wheels:",self.wheels)

class Car(Vehicle):
    def __init__(self, brand, wheels,yearof_release):
        Vehicle().__init__(brand, wheels)
        self.yearof_release=yearof_release
    def getcarinfo(self):
        print("Year of release:",self.yearof_release)

class Plane(Vehicle):
    def __init__(self, brand, wheels,name):
        Vehicle().__init__(brand, wheels)
        self.name=name
    def getplaneinfo(self):
        print("Name of plane:",self.name)

class FlyingCar(Car,Plane):
    def __init__(self, brand, wheels, yearof_release,height_limit,flying_speed):
        Car().__init__(brand, wheels, yearof_release)
        self.height_limit=height_limit
        self.flying_speed=flying_speed
    def getflyingcarinfo(self):
        print("Height limit is :",self.height_limit)
        print("Flying speed is :",self.flying_speed)

fc=FlyingCar("BMW",4,2007,5000,300)
fc.getflyingcarinfo()
fc.getcarinfo()
fc.getplaneinfo()





class Person:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
    def personinfo(self):
        print("Person Name:",self.name)
        print("Person's Designation:",self.designation)
class Employee(Person):
    def __init__(self, name, designation,empname,empdesignation):
        super().__init__(name, designation)
        self.empname=empname
        self.empdesignation=empdesignation
    def empinfo(self):
        print("Employee Name:",self.empname)
        print("Employee Designation:",self.empdesignation)
class Hr(Employee):
    def __init__(self, name, designation, empname, empdesignation,hrname,responsibilities):
        super().__init__(name, designation, empname, empdesignation)
        self.hrname=hrname
        self.responsibilities=responsibilities
    def hrinfo(self):
        super().personinfo()
        super().empinfo()
        print("HR Name:",self.hrname)
        print("Responsibilities:",self.responsibilities)
class Manager(Employee):
    def __init__(self, name, designation, empname, empdesignation,mgrname,mgrsal):
        super().__init__(name, designation, empname, empdesignation)
        self.mgrname=mgrname
        self.mgrsal=mgrsal
    def managerinfo(self):
        super().personinfo()
        super().empinfo()
        print("Manager Name:",self.mgrname)
        print("Manager Salary:",self.mgrsal)

hr1=Hr("akshitha","sde","akshu","trainee","Rafik","hiring")
hr1.hrinfo()
print("----------------------------------------------------------------------------------")
mgr1=Manager("nandhitha","Analyst","samhitha","content moderation","Venkateshwarlu",80000)
mgr1.managerinfo()

'''

class Vehicle:  
    def __init__(self, name, color):  
        self.name = name  
        self.color = color  
  
    def transport(self):  
        print("The name of the vehicle:", self.name)  
        print("The color of the vehicle:", self.color)  
  
class Car(Vehicle):  
    def __init__(self, name, color, speed, wheels):  
        Vehicle.__init__(self,name, color)  
        self.speed = speed  
        self.wheels = wheels  
  
    def transport(self):  
        Vehicle.transport(self) 
        print("The speed of the car is:", self.speed)  
        print("The number of wheels is:", self.wheels)  
  
class Plane(Vehicle):  
    def __init__(self, name, color, fname, ftype):  
        Vehicle.__init__(self,name, color)  
        self.fname = fname  
        self.ftype = ftype  
  
    def transport(self):  
        Vehicle.transport(self) 
        print("The name of the plane is:", self.fname)  
        print("The type of the plane is:", self.ftype)  
  
class Flyingcar(Car, Plane):  
    def __init__(self, name, color, speed, wheels, fname, ftype, fspeed, heightlim):  
        Car.__init__(self, name, color, speed, wheels)    
        Plane.__init__(self, name, color, fname, ftype)  
        self.fspeed = fspeed  
        self.heightlim = heightlim  
  
    def transport(self):  
        Car.transport(self)  
        Plane.transport(self)  
        print("The flying speed is:", self.fspeed)  
        print("The height limit is:", self.heightlim)  
  
f = Flyingcar("bmw", "Red", 120, 4, "falcon", "hybrid", 300, 10000)  
f.transport()
