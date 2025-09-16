'''
class A:
    def demo(self):
        print("class A")
class B:
    def task(self):
        print("Class B")
class C(A,B):
    def driver(self):
        print("class C")
c=C()
c.demo()
c.task()
c.driver()


class A:
    def __init__(self,work,timings):
        self.work=work
        self.timings=timings
        print("Work Type:",self.work)
        print("Timings:",self.timings)
    def demo(self):
        print("Work has to be done by the person")
class B:
    def __init__(self,responsibilities,salary):
        self.responsibilities=responsibilities
        self.salary=salary
        print("Responsibilities: ",self.responsibilities)
        print("Salary: ",self.salary)
    def task(self):
        print("Tasks should be completed on time")
class C(A,B):
    def __init__(self, work, timings,responsibilities,salary,bond,location):
        super().__init__(work, timings)
        super().__init__(responsibilities,salary)
        self.bond=bond
        self.location=location
    def driver(self):
        print("Vehicle should be maintained neatly")
c=C("Driver","9 am to 9 pm","accept rides, drive safely",35000,"2 years","Hyd")
c.demo()
c.task()
c.driver()


class Sample:
    def m1(self):
        print("m1 function from Sample")

class Sample1:
    def m1(self):
        print("m1 function from Sample1")

class MainClass(Sample,Sample1):
    def m2(self):
        print("m2 function from MainClass")

m=MainClass()
m.m1()
m.m2()
'''


class Sample:
    def __init__(self,a1):
        self.a1=a1
    def m1(self):
        print("m1 function from Sample",self.a1)

class Sample1:
    def __init__(self,a2):
        self.a2=a2
    def m2(self):
        print("m1 function from Sample1",self.a2)

class MainClass(Sample,Sample1):
    def __init__(self, a1,a2,a3):
        super().__init__(a1)
        super().__init__(a2)
        self.a3=a3
    def m3(self):
        print("m2 function from MainClass",self.a3)

m=MainClass(2,3,4)
m.m1()
m.m2()
m.m3()


