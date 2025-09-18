'''
class Student:
    def stdinfo(self,name,std_id):
        print(name)
        print(std_id)
        print(id(self))
s1=Student()
s1.stdinfo("KANE",1209)
print(id(s1))
print("*"*20)
s2=Student()
s2.stdinfo("Jinny",1234)
print(id(s2))
print("*"*20)
s3=Student()
s3.stdinfo("Bunny",2234)
print(id(s3))
print("*"*20)
'''

class Laptop:
    def __init__(self):
        print("No argument Constructor")
l1=Laptop()

class employee:
    def __init__(self,name,sal):
        print(name)
        print(sal)
E1=employee("Akshitha",100000)

class demo:
    print("Akshitha")
    print("I am pursuing MCA")
d1=demo()

