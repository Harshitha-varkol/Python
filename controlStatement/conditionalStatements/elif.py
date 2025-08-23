print("RESULT OF STUDENTS")
marks = int(input("Enter marks:"))
if marks>=35 and marks<=50:
	print("JUST PASS")
elif marks>50 and marks<=70:
	print("FIRST CLASS PASS")
elif marks>70 and marks<=90:
	print("DISTINCTION")
elif marks>90 and marks<=100:
	print("TOPPER")
else:
	print("FAIL")

print("FLIGHT PRICES")
price=int(input("Enter the price:"))
if price>=3000 and price<=5000:
	print("Normal SEAT")
elif price>5000 and price<=10000:
	print("VIP")
elif price>10000 and price<=50000:
	print("Business class")
else:
	print("No seat avaible for your price")

#WAPP that categorizes a person's age into child(0-12) , teenager(13-19), adult(20-64),senior(65+)

age= int(input("Enter the age:"))
if age>0 and age<=12:
	print("CHILD")
elif age>12 and age<=19:
	print("TEENAGER")
elif age>19 and age<=64:
	print("ADULT")
elif age>=65:
	print("SENIOR")

num1=int(input("Enter digit 1:"))
num2=int(input("Enter digit 2:"))
operation=input("Enter the operation you want to perform (+,-,*,//):")
if operation=="+":
	print(num1+num2)
elif operation=="-":
	print(num1-num2)
elif operation=="*":
	print(num1*num2)
elif operation=="//":
	print(num1//num2)
else:
	print("Invalid number or operation")


num=int(input("Enter a number:"))
if num>0:
	print("POSITIVE")
	if num%2==0:
		print("EVEN")
	else:
		print("ODD")
elif num<0:
	print("NEGATIVE")
elif num==0:
	print("ZERO")
else:
	print("INVALID")

character=input("Enter a character:")
char=ord(character)
if char in (65,69,73,79,85,97,101,105,111,117):
	print("Vowel")
elif (65 <= char <= 90 or 97 <= char <= 122) and char not in (65,69,73,79,85,97,101,106,111,117):
	print("Consonant")
elif (48<=char<=57):
	print("Digit")

