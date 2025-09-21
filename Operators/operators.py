"""
Name = "Desktop- NRAA2E1"
Storage = "8.00 GB"
Color="black"
Type = "64-bit operating system, x64-based processor"
Version = "Windows 10 Pro"
print("My Laptop name is "+ Name)
print(id(Name))
print(type(Name))
print("Color of my laptop is ",Color)
print(id(Color))
print(type(Color))
print("The storage is ",Storage)
print(id(Storage))
print(type(Storage))
print("Laptop type is ",Type)
print(id(Type))
print(type(Type))
print("Version is ",Version)
print(id(Version))
print(type(Version))

a=305
b=300
res= print("smallest number is: ,a") if a<b else print("smallest number is : ",b)
print(res)

a=300
b=400
res = a if a>b else b
print(res)

a=100
b=1000
c=500
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(b<=a)
print(b>=a)
print(a>b and a>c)
print(c>a or c>b)
print(not(c>a))

num1=100
num1+=num1
num1-=100
num1*=4
num1/=5
num1//3
num1**=2
print(num1)



a2=30
b2=42
c2=52
res1 = a2 if (a2>b2 and a2>c2) else b2 if (b2>a2 and b2>c2) else c2
print("largest number is : ",res1)

a3=34
b3=23
c3=98
res3= a3 if (a3<b3 and a3<c3) else b3 if (b3<a3 and b3<c3) else c3
print("Smallest number is : ",res3)


num1=10
num2=20
"""

b=0
for i in range(48,58):
	print("{} = {}".format(chr(i),i))

i=65
for i in range(65,91):
	print("{} = {}".format(chr(i),i))

a=97
for i in range(97,123):
	print("{} = {}".format(chr(i),i))