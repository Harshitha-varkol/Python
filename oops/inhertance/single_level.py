'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getpersoninfo(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Employee(Person):
    def __init__(self,name,age,id,dept,sal):
        super().__init__(name,age)
        self.id=id
        self.dept=dept
        self.sal=sal
    def getempinfo(self):
        super().getpersoninfo()
        print("Id:",self.id)
        print("Dept:",self.dept)
        print("Sal:",self.sal)
e1=Employee("Akshu",21,123,34,75000)
e1.getempinfo()

class Animal:
    def __init__(self,warmblood):
        self.warmblood=warmblood
    def get_warmblood(self):
        print("Has Warmblood:",self.warmblood)
    def swim(self):
        print("Animals Can Swim")
class Cat(Animal):
    def __init__(self, warmblood):
        super().__init__(warmblood)
    def meow(self):
        super().get_warmblood()
        # super().swim()
        print("Cat says MEOW")
c1=Cat("YES")
c1.meow()
c1.swim()
print("--"*20)
class Bird:
    def __init__(self,warmblood):
        self.warmblood=warmblood
    def get_warmblood(self):
        print("Has Warmblood:",self.warmblood)
    def swim(self):
        print("Can Swim")
    def fly(self):
        print("Can Fly")
class Duck(Bird):
    print("DUCK PROPERTIES AND BEHAVIOURS")
    def __init__(self,warmblood,color,age):
        super().__init__(warmblood)
        self.color=color
        self.age=age
    def getcatinfo(self):
        super().get_warmblood()
        super().swim()
        super().fly()
d=Duck("Yes","Grey",10)
d.getcatinfo()
'''

class Snapchat:
    def __init__(self,login_id,user_name):
        self.login_id=login_id
        self.user_name=user_name
        print("SNAPCHAT")
    def snapchat_info(self):
        print("LOGIN ID =",self.login_id)
        print("USERNAME =",self.user_name)
class User(Snapchat):
    def __init__(self, login_id, user_name,password):
        super().__init__(login_id, user_name)
        self.password=password
        print("USER DETAILS")
    def snapchat_info(self):
        super().snapchat_info()
        print("PASSWORD =",self.password)
u1=User("akshu123","AkshithaVangari","akshu@123")
u1.snapchat_info()