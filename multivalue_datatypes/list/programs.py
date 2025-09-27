#wapp to calculate the avg of numbers in a given list
l1=eval(input("Enter a list:"))
sum=0
for i in l1:
    sum+=i
avg=sum//len(l1)
print("Average of numbers in the list:",avg)

#wapp to find the second largest number in a tuple
t1=(5,1,4,3,6,2)
l1=list(t1)
l2=sorted(l1)
t2=tuple(l2)
print("Second largest number is:",t2[-2])

#wapp to merge two lists and sort it

l1=[1,2,3,4,5]
l2=[2,3,4,5,6,7]
l3=l1+l2
print(l3)
l3.sort()
print(l3)

#wapp to swap the first and last value of a list
l1=[1,2,3,4,5]
l1[0],l1[-1]=l1[-1],l1[0]
print(l1)

#wapp to remove duplicates items from a list
l1=[1,2,3,3,4,5,4,6,6,6,5,4,4,3,2,2,4,8,7,7]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

#wapp to find largest element in a list
l1=[23,45,100,456,999,30]
l1.sort()
print("Largest element in list is:",l1[-1])

#wapp to find smallest element in the list
l1=[23,45,100,456,999,30]
l1.sort()
print("Smallest element in list is:",l1[0])


