#for most of the digit related programs use WHILE loop
#1
num=int(input("Enter number:"))
count=0
while(num>0):
	#rem=num%10 it is optional good to use for better understanding
	count+=1
	num//=10
print(count)
print(num)

#2
num=int(input("ENTER NUM:"))
while num>0:
	rem=num%10
	if rem%2==0:
		print(rem)
	num=num//10

#3
num=int(input("Enter num:"))
sum=0
while num>0:
	rem=num%10
	sum+=rem
	num//=10
print(sum)

#4
num=int(input("Enter number:"))
count=0
while num>0:
	rem=num%10
	if rem%2==0:
		count+=1
	num//=10
print(count)

#5
num=int(input("Enter number:"))
count=0
while num>0:
	rem=num%10
	if rem%2==1:
		count+=1
	num//=10
print(count)

#6
num=int(input("Enter number:"))
sum=0
while num>0:
	rem=num%10
	if rem%2==0:
		sum+=rem
	num//=10
print(sum)

#7
num=int(input("Enter number:"))
sum=0
while num>0:
	rem=num%10
	if rem%2==1:
		sum+=rem
	num//=10
print(sum)

#8
num=int(input("Enter num:"))
even_sum=0
odd_sum=0
while num>0:
	rem=num%10
	if rem%2==0:
		even_sum+=rem
	else:
		odd_sum+=rem
	num//=10
print(even_sum)
print(odd_sum)

#9
i=1
while(i<101):
	print(i)
	i+=1

#10
num=int(input("Enter num:"))
largest_num=0
while num>0:
	rem=num%10
	if rem>largest_num:
		largest_num=rem
	num//=10
print(largest_num)