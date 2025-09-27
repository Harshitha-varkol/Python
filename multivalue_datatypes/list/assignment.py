print("WAPP to find sum of all the elements in the list")

l1=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in l1:
    sum+=i
print(sum)

print("WAPP to find sum of 1st and last element in the list")
l1=[1,2,3,4,5]
l2=l1[0]
l3=l1[-1]
print(l2+l3)

print("WAPP to sort list in ascending order without using inbuilt function")
l1=[13,9,88,44,55]
for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp
print(l1)


print("WAPP to sort list in descending order without using inbuilt function")
l1=[13,9,88,44,55]
for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]<l1[j]:
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp
print(l1)

print("WAPP to check vowels present in the list")
l1=["a","e","d","t","u"]
l2=list()
s1="aeiouAEIOU"
for i in l1:
    if i in s1:
        l2.append(i)
print(l2)

print("WAPP to merge two list without using inbuilt function")
l1=[1,2,3,4,5,5,6]
l2=[6,7,8,9]
l3=l1+l2
print(l3)


print("WAPP to print common element in two lists")
l1=[1,2,3,4,5]
l2=[4,5,6,7,8,9]
l3=[]
for i in l1:
    if i in l2 and i not in l3:
        l3.append(i)
print(l3)

l1=[1,2,3,3,4,2,3,4]
s1=set()
for i in l1:
    s1.add(i)
print(s1)
for i in s1:
    count=0
    for j in l1:
        if i==j:
            count+=1
    print(i,":",count)

str1=input("Enter a string:")
s1=set()
for i in str1:
    s1.add(i)
print(s1)
for i in s1:
    count=0
    for j in str1:
        if i==j:
            count+=1
    print(i,":",count)