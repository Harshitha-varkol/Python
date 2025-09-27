print("WAPP to print even index element in list")
l1=[1,2,3,4,5,55,6,6777]
l2=[]
for i in range(0,len(l1)):
    if i%2==0:
        l2.append(l1[i])
print(l2)

print("WAPP to print odd index element in a list")
l1=[1,2,3,4,5,55,6,6777]
l2=[]
for i in range(0,len(l1)):
    if i%2!=0:
        l2.append(l1[i])
print(l2)

print("WAPP to print each element of list according to their index value")
l1=["kane","jinny","bunny"]
for i in range(0,len(l1)):
    print(i,":",l1[i])

print("WAPP to print only prime element in list")
l1=[1,3,2,4,7,11,13,55,15]
l2=[]
for i in l1:
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        l2.append(i)
print(l2)

print("WAPP to count palindrome element in list")
s1={123,121,253,353,444,505,789}
s2=set()
count=0
for i in s1:
    num=i
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    if rev==i:
        count+=1
        s2.add(i)
print(s2)
print("Number of palindrome elements:",count)


print("WAPP to find factorial of each element in tuple")
t1=(1,5,3,7,2)
for i in t1:
    fact=1
    for j in range(i,0,-1):
        fact+=fact*j
    print(i,":",fact)

print("WAPP to count armstrong numbers from tuple")
t1=(123,153,196,9474)
t2=()
count=0
for i in t1:
    sum=0
    num=i
    num1=i
    count1=0
    while num>0:
        count1+=1
        num//=10
    while num1>0:
        rem=num1%10
        pow=rem**count1
        sum+=pow
        num1//=10
    if sum==i:
        count+=1
        print(i)
print("Number of armstrong numbers:",count)

print("WAPP to create an empty tuple in python")
t1=()
print(t1)

print("WAPP to create a tuple with mixed data types")
t1 = (25, "Hello", 3.14, True)
print(t1)

print("How do you access third element of a tuple")
t1 = (25, "Hello", 3.14, True)
print(t1[2])