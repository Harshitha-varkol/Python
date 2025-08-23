
print(" 2 table")
for i in range(1,11):
	#print("2*{}={}".format(i,2*i))
	print("2","*",i,"=",2*i)

print("natural numbers")
for i in range(1,11):
	print(i)

print("sum of natural numbers")
sum=0
for i in range(1,11):
	sum+=i
print(sum)

print("sum of even num")
sum=0
for i in range(1,11):
	if i%2==0:
		sum+=i
print(sum)

print("sum of odd num")
sum=0
for i in range(1,11):
	if i%2==1:
		sum+=i
print(sum)

print("even numbers")
for i in range(1,11):
	if i%2==0:
		print(i)

print("odd numbers")
for i in range(10,0,-1):
	if i%2==1:
		print(i)

num=int(input("Enter num:"))
count=0
for i range(1,num+1):
	if num%i==0:
		count+=1
print(count)

num=int(input("Enter num:"))
count=0
for i in range(1,num+1):
	if num%i==0:
		count+=1
if count==2:
	print("Prime Number")
else:
	print("Not a prime number")


num=int(input("Enter num:"))
count=0
for i in range(1,num+1):
	if num%i==0:
		count+=1
if count!=2:
	print("Composite Number")
else:
	print("Not a composite number")


num=50
for i in range(2,num):
	for j in range(2,i):
		if i%j==0:
			break
	else:
		print(i,end=',')


for i in range(65,91):
	print(chr(i))

for i in range(97,123):
	print(chr(i))