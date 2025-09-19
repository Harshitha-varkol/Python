'''
#perfect numbers from 1 to 100
#perfect numbers = the sum of the factors excluding the number taken must be equal to the number itself
#ex: 6 => factors : 1,2,3 

for j in range(1,101):
	sum=0
	for i in range(1,j):
		if j%i==0:
			sum+=i
	if sum==j:
		print(j)

#count of perfect numbers from 1 to 100

count=0
for j in range(1,101):
	sum=0
	for i in range(1,j):
		if j%i==0:
			sum+=i
	if sum==j:
		count+=1
print("Number of perfect numbers between 1 to 100 :",count)

#sum of perfect numbers from 1 to 100

sum_pn=0
for j in range(1,101):
	sum=0
	for i in range(1,j):
		if j%i==0:
			sum+=i
	if sum==j:
		sum_pn+=j
print(sum_pn)


#wapp to check if number is divisible by 3 , print FIZZ . If the number is divisible by 5 , print BUZZ . If the number is divisible by both 3 and 5 print FIZZ and BUZZ . Otherwise print the number itself

num=int(input("ENTER NUM:"))
if num%3==0 and num%5==0:
	print("FIZZ BUZZ")
elif num%3==0:
	print("FIZZ")
elif num%5==0:
	print("BUZZ")
else:
	print(num)
#WAPP to check the given year is leap year or not

for Year in range(2000,2026):
	if Year%4==0 and (Year%100!=0 or Year%400==0):
		print(Year)


#factorial
num=int(input("Enter num:"))
fact=1
for i in range(1,num+1):
	fact=fact*num
	num-=1
print(fact)


for r in range(1,11):
	fact=1
	for i in range(1,r+1):
		fact=fact*i
	print(r,":",fact)


sum=0
for r in range(1,11):
	fact=1
	for i in range(1,r+1):
		fact=fact*i
	sum+=fact
print(sum)


n=int(input("Enter num:"))
while n>0:
	rem=n%10
	fact=1
	for i in range(1,rem+1):
		fact=fact*i
	print(rem,":",fact)
	n//=10


sum=0
n=int(input("Enter num:"))
while n>0:
	rem=n%10
	fact=1
	for i in range(1,rem+1):
		fact=fact*i
	sum+=fact
	n//=10
print(sum)

sum=0
n=int(input("Enter num:"))
n1=n
while n>0:
	rem=n%10
	fact=1
	for i in range(1,rem+1):
		fact=fact*i
	sum+=fact
	n//=10
if sum==n1:
	print(n1,"is strong number")
else:
	print(n1,"is not a strong number")


for n in range(1,1001):
	sum=0
	n1=n
	while n>0:
		rem=n%10
		fact=1
		for i in range(1,rem+1):
			fact=fact*i
		sum+=fact
		n//=10
	if sum==n1:
		print(n1)

for n in range(1,1001):
	sum=0
	n1=n
	while n>0:
		rem=n%10
		fact=1
		for i in range(1,rem+1):
			fact=fact*i
		sum+=fact
		n//=10
	if sum==n1:
		print(n1)

#spy number
num=int(input("Enter num:"))
num1=num
num2=num
sum=0
while num1>0:
    rem=num1%10
    sum+=rem
    num1//=10
print("sum of digits:",sum)
product=1
while num2>0:
    rem1=num2%10
    product*=rem1
    num2//=10
print("product of digits:",product)
if sum==product:
    print("SPY NUMBER")
else:
    print("NOT A SPY NUMBER")
    
#spy numbers from 1 to 1000
for num in range(1,10001):
    num1=num
    num2=num
    sum=0
    while num1>0:
          rem=num1%10
          sum+=rem
          num1//=10
    product=1
    while num2>0:
          rem1=num2%10
          product*=rem1
          num2//=10
    if sum==product:
          print(num)
         
#sunny number
num=int(input("Enter num:"))
for i in range(1,num+1):
    square=i**2
    if square==(num+1):
    	 print("SUNNY NUMBER")
          
#sunny numbers from 1 to 1000
for i in range(1,1001):
	for j in range(1,i+1):
		square=j**2
		if square==(i+1):
			print(i)

#sunny numbers sum from 1 to 1000
sum=0
for i in range(1,1001):
	for j in range(1,i+1):
		square=j**2
		if square==(i+1):
			sum+=i
print(sum)

#Harshad number or Niven number
num=int(input("Enter num:"))
num1=num
sum=0
while num>0:
	rem=num%10
	sum+=rem
	num//=10
if num1%sum==0:
	print("HARSHAD NUMBER")
else:
	print("NOT A HARSHAD NUMBER")

#Harshad numbers from 1 to 1000,count,sum
count=0
sum1=0
for i in range(1,1001):
	num1=i
	sum2=0
	while num1>0:
		rem=num1%10
		sum2+=rem
		num1//=10
	if i%sum2==0:
		print(i)
		count+=1
		sum1+=i
print(count)
print(sum1)

#Happy Number
num=int(input("Enter num:"))
sum=0
while num!=1:
    rem=num%10
    sum+=rem**2
    num//=10
    if sum!=1:
        num=sum
        sum=0
    elif sum==1:
        print("Happy number")
    else:
        print("Not a Happy number ")
	

#Xylem Number
n=int(input("enter any number"))
no=n
sum1=0
rem=n%10
sum1+=rem
n=n//10
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
rem=rev%10
sum1+=rem
rev=rev//10
sum2=0
while rev>0:
    rem=rev%10
    sum2+=rem
    rev=rev//10
print(sum1)
print(sum2)
if sum1==sum2:
    print("xylem number",no)
else:
    print("phloem number",no)

#xylem numbers from 1 to 1000   
for n in range(1,1001):
    no=n
    sum1=0
    rem=n%10
    sum1+=rem
    n=n//10
    rev=0
    while n>0:
         rem=n%10
         rev=rev*10+rem
         n=n//10
    rem=rev%10
    sum1+=rem
    rev=rev//10
    sum2=0
    while rev>0:
         rem=rev%10
         sum2+=rem
         rev=rev//10
    # print(sum1)
    # print(sum2)
    if sum1==sum2:
         print(no)

#CHECK WHETHER 2 NUMBERS ARE TWIN PRIMES OR NOT 
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
count=0
for i in range(1,num1+1):
    if num1%i==0:
        count+=1
if count==2:
    count1=0
    for i in range(1,num2+1):
        if num2%i==0 and (num2==num1+2 or num2==num1-2):
            count1+=1
    if count1==2:
          print(num1,",",num2,"are TWIN PRIMES")
else:
	print("Not twin primes")
        
#TWIN PRIMES FROM 1 to 1000
total_count=0
for num in range(1,1000):
	count=0
	for i in range(1,num+1):
		if num%i==0:
			count+=1
	if count==2:
		num1=num+2
		count1=0
		for i in range(1,num1+1):
			if num1%i==0:
				count1+=1
		if count1==2:
			print(num,",",num1)
			total_count+=1
print(total_count)

a1=[10,8,7,5,6,3]
for j in range(len(a1)):
    for i in range(len(a1)-1):
        if a1[i]<a1[i+1]:
                swap=a1[i]
                a1[i]=a1[i+1]
                a1[i+1]=swap
print(a1)

a1=[10,8,7,5,6,3]
for j in range(len(a1)):
    for i in range(len(a1)-1):
        if a1[i]>a1[i+1]:
                swap=a1[i]
                a1[i]=a1[i+1]
                a1[i+1]=swap
print(a1)


#DISARIUM NUMBER
num=int(input("Enter num:"))
num1=num
num2=num
count=0
sum=0
while num>0:
    rem=num%10
    count+=1
    num//=10
while num1>0:
    pow=1
    rem1=num1%10
    num1//=10
    for i in range(1,count+1):
        pow*=rem1
    sum+=pow
    count-=1
if num2==sum:
    print("Disarium Number")
else:
    print("Not a Disarium number")
    
#DISARIUM NUMBERS FROM 1 to 1000
for num in range(1,1001):
    num1=num
    num2=num
    count=0
    sum=0
    while num1>0:
         rem=num1%10
         count+=1
         num1//=10
    while num2>0:
         pow=1
         rem1=num2%10
         num2//=10
         for i in range(1,count+1):
              pow*=rem1
         sum+=pow
         count-=1
    if num==sum:
         print(num)
         
#PRINT FIRST HALF OR LAST HALF OF THE NUMBER:
num=123456
num1=num
count=0
while num1>0:
    rem=num1%10
    count+=1
    num1//=10
print(count)
half=count//2
num2=10**half
print(num2)
num3=num
num3=num3//num2
num4=num
num4=num4%num2
print(num3)
print(num4)

#FINDING POWER
num=int(input("Enter NUM:"))
power1=int(input("Enter power:"))
for i in range(1,power1):
	num*=num
print(num)


count=0
num=int(input("Enter num:"))
num1=num
while num>0:
	rem=num%10
	count+=1
	
	num//=10
while num1>0:
	rem1=num1%10
	num2=rem1**count
	print(rem1,":",num2)
	num1//=10


count=0
num=int(input("Enter num:"))
num1=num
while num>0:
	rem=num%10
	count+=1
	num//=10
while num1>0:
	num2=1
	rem1=num1%10
	num1//=10
	for i in range(1,count+1):
		num2*=rem1
	print(rem1,":",num2)


count=0
num=int(input("Enter num:"))
num1=num
no=num
while num>0:
	rem=num%10
	count+=1
	num//=10
sum=0
while num1>0:
	num2=1
	rem1=num1%10
	for i in range(1,count+1):
		num2*=rem1
	sum+=num2
	num1//=10
if no==sum:
	print("Armstrong Number")
else:
	print("Not an Armstrong Number")

#02-05-2025
#METHOD - 1
#wapp to print all the armstrong numbers from 1 to 1000
#1
print("print all the armstrong numbers from 1 to 1000")
for num in range(1,1001):
	count=0
	num1=num
	num3=num1
	while num1>0:
		rem=num1%10
		count+=1
		num1//=10
	sum=0
	while num3>0:
		num2=1
		rem1=num3%10
		num2=rem1**count
		sum+=num2
		num3//=10
	if num==sum:
		print(num)

#METHOD = 2
for num in range(1,1001):
	count=0
	num1=num
	no=num1
	while num1>0:
		count+=1
		num1//=10
		#print(count)
	sum=0
	while no>0:
		num2=1
		rem=no%10
		for i in range(1,count+1):
			num2=num2*rem
		sum+=num2
		no//=10
	if num==sum:
		print(num)

#2
#count of armstrong numbers from 1 to 1000
print("count of armstrong numbers from 1 to 1000")
count_of_ano=0
for num in range(1,1001):
	count=0
	num1=num
	num3=num1
	while num1>0:
		rem=num1%10
		count+=1
		num1//=10
	sum=0
	while num3>0:
		num2=1
	
		rem1=num3%10
		num2=rem1**count
		sum+=num2
		num3//=10
	if num==sum:
		count_of_ano+=1
print("Number of armstrong numbers from 1 to 1000:",count_of_ano)


#3
#sum
print("sum of armstrong numbers from 1 to 1000")
sum_of_ano=0
for num in range(1,1001):
	count=0
	num1=num
	num3=num1
	while num1>0:
		rem=num1%10
		count+=1
		num1//=10
	sum=0
	while num3>0:
		num2=1
		rem1=num3%10
		num2=rem1**count
		sum+=num2
		num3//=10
	if num==sum:
		sum_of_ano+=num
print("Sum of armstrong numbers from 1 to 1000:",sum_of_ano)

#4
#WAPP to print reverse of a number
print("reverse of number")
num=int(input("Enter num:"))
rev=0
num1=num
while num>0:
	rem=num%10
	rev=rev*10+rem
	num//=10
print(rev)

#5
print("Checking whether number is palindrome or not")
num=int(input("Enter num:"))
rev=0
num1=num
while num>0:
	rem=num%10
	rev=rev*10+rem
	num//=10
print(rev)
if num1==rev:
	print(num1 ,"is PALINDROME")
else:
	print(num1 ,"is not a PALINDROME"
	)

#6
#wapp to print no of palindromes from 1 to 1000
print("palindromes from 1 to 1000")
for num in range(1,1001):
	rev=0
	num1=num
	while num>0:
		rem=num%10
		rev=rev*10+rem
		num//=10
	if num1==rev:
		print(num1)
		
#7
print("Count of palindromes from 1 to 1000")
count=0
for num in range(1,1001):
	rev=0
	num1=num
	while num>0:
		rem=num%10
		rev=rev*10+rem
		num//=10
	if num1==rev:
		count+=1
		sum+=num1
print("NUMBER OF PALINDROMES FROM 1 to 1000: ",count)

#8
print("Sum of Palindromes from 1 to 1000")
sum=0
for num in range(1,1001):
	rev=0
	num1=num
	while num>0:
		rem=num%10
		rev=rev*10+rem
		num//=10
	if num1==rev:
		sum+=num1
print("SUM OF PALINDROME NUMBERS FROM 1 to 1000:",sum)


num=int(input("Enter num:"))
power=int(input("Enter power:"))
pow=1
for i in range(1,power+1):
	pow=pow*num
print(pow)


