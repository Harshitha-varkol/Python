
print("WAPP count how many numbers are greater than 10 in a list")
l1=[1,2,30,560,60,70,3,5,80]
count=0
for i in l1:
    if i>10:
        count+=1
print(count)

print("WAPP to print only positive numbers from a list")
l1=[1,5,3,4,-2,-3,4,8]
l2=[]
for i in l1:
    if i>0:
        l2.append(i)
print(l2)

print("WAPP to check the given two strings are anagram or not")
#method1
s="listen"
s1="silent"
l1=len(s)
l2=len(s1)
lit1=list(s)
lit2=list(s1)
for i in lit1:
    if l1==l2 and i in lit2:
        print("it is anagram")
        break
    else:
        print("it is not")
        break

#method2
s1 = "Ansar"
s2 = "Rasna"
if sorted(s1.lower()) == sorted(s2.lower()):
    print("anagram")
else:
    print("Not an anagram")

print("WAPP to merge and sort two lists")
l1=[1,7,5,6,4]
l2=[9,10,2]
l3=l1+l2
print(l3)
# print(sorted(l3))
for i in range(0,len(l3)):
    for j in range(i+1,len(l3)):
        if ((l3[i]))>((l3[j])):
            l3[i],l3[j]=l3[j],l3[i]
print(l3)


print("WAPP to find largest string in a list")
l1=["helloooo","hell","helloo"]
for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if (len(l1[i]))>(len(l1[j])):
            l1[i],l1[j]=l1[j],l1[i]
print(l1[-1])

print("WAPP to print duplicates in a list")
l1=[1,2,3,4,5,5,6,7,7,4,4,3]
l2=[]
for i in l1:
    count=0
    for j in l1:
        if i==j:
            count+=1
    if count>=2:
        if i not in l2:
            l2.append(i)
print(l2)

print("WAPP to remove negative numbers from a list")
l1=[1,2,-1]
for i in l1:
    if i<0:
        l1.remove(i)
print(l1)

print("WAPP to convert list into a set")
l1=[1,2,3,4,5,6,7]
s1=set(l1)
print(s1)

print("WAPP to print all even numbers from a list")
l1=[2,3,4,5,6,7,8]
l2=[]
for i in l1:
    if i%2==0:
        l2.append(i)
print(l2)

print("WAPP to print all odd numbers from a list")
l1=[2,3,4,5,6,7,8]
l2=[]
for i in l1:
    if i%2!=0:
        l2.append(i)
print(l2)


print("WAPP to split a list into 2 parts")
l1=[2,3,4,5,6,7,8,9]
l2=l1[:(len(l1)//2)]
print(l2)
l3=l1[((len(l1)//2)):]
print(l3)

l1=[2,3,4,5,6,7,8,9]
length=len(l1)//2
l2=[]
l3=[]
for i in range(0,len(l1)):
    if i<length:
        l2.append(l1[i])
    else:
        l3.append(l1[i])
print(l2)
print(l3)


print("WAPP to check if a list is empty or not")
l1=[1,2,3,4,5,5]
if len(l1)==0:
    print("Empty")
else:
    print("Not empty")

print("WAPP to reverse a list without using inbuilt function")
l1=[1,2,3,4,5]
l2=l1[-1::-1]
print(l2)

print("WAPP to find largest and smallest elements in a list without using inbuilt function")
l1=[1,2,3,4,5]
largest=0
for i in l1:
    if i>largest:
        largest=i
print("largest element:",largest)
smallest=largest
for i in l1:
    if i<smallest:
        smallest=i
print("smallest element:",smallest)


