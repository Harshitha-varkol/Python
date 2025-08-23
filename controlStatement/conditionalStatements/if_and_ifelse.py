'''
#1
num=int(input("Enter a number:"))
if (num%2==0 and num%6==0):
	print("DIVISIBLE")
	num = complex(num)
	print(num)

#2
num=int(input("Enter a number:"))
if num%5==0:
	print("Given number is a multiple of 5")
else:
	print("Not a multiple of 5")

#3
num=int(input("Enter a number:"))
if num==0:
	print(num)

#4
num=int(input("Enter a number:"))
if num<0:
	print("NEGATIVE")

#5
num=int(input("Enter a number:"))
if num%2==0:
	num+=1
	print(num)

#6 WAPP to check if a number is positive?
num=int(input("Enter a number:"))
if num>0:
	print("POSITIVE")

#7 WAPP to check if a number is even or odd
num=int(input("Enter a number:"))
if num%2==0:
	print(num, "is even number")
else:
	print(num, "is odd number")

#8 WAPP that checks if a given number is divisible by 5
num = int(input("Enter a number:"))
if num%5==0:
	print(num ,"is divisible by 5")

#9 WAPP to check if the user input age is elgible for voting

age = int(input("Enter AGE:"))
if age>=18:
	print("Eligible to vote")
else:
	print("Not eligible to vote")

#10 WAPP to check if a given string is "Hello"?

str1= input("Enter a string:")
if str1=="Hello":
	print("The string is Hello")

#WAPP to check if a number is positive or negative

num=int(input("Enter a number:"))
if num>0:
	print(num,"is positive")
else:
	print("Negative or Zero")

#WAPP to find the max of 2 numbers

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
if a>b:
	print(a,"is greater than",b)
else:
	print(b,"is greater than",a)
'''

Year=int(input("Enter year:"))
if Year%4==0 and (Year%100!=0 or Year%400==0):
	print("LEAP YEAR")
else:
	print("NOT A LEAP YEAR")


#CHECK WHETHER AADHAR NUMBER IS VALID OR NOT
aadhar=int(input("Enter aadhar num:"))
count=0
#num=aadhar
while aadhar>0:
	rem=aadhar%10
	count+=1
	
	aadhar//=10
if count==12:
	print("Your aadhar number is valid")
else:
	print("Your aadhar number is not valid")
