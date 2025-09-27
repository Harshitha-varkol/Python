print("WAPP to add objects into a list")
class Student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
    def getstudentinfo(self):
        return self.name+":"+self.id+":"+self.age

l=[]
while True:
    name=input("Enter name:")
    id=input("Enter id:")
    age=input("Enter age:")
    s1=Student(name,id,age)
    l.append(s1.getstudentinfo())
    n=int(input("Enter 1 to repeat , 2 to terminate"))
    if n==1:
        continue
    else:
        break
print("number of objects:",len(l))
for i in l:
    print(i)
