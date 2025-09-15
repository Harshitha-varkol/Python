
#print("*"*4)

#1
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        print("*",end=' ')
    print()
#2
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        print("@",end=' ')
    print()

#3
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        print("A",end=' ')
    print()

#4
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        print(i,end=' ')
    print()

#5
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        print(j,end=' ')
    print()

#6
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        print(i+j,end=' ')
    print()

#7
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        print(i%2,end=' ')
    print()

#8
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        print(j%2,end=' ')
    print()

#9
no=1
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        print(no,end=' ')
        no+=1
    print()

#try
no=1
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        print(no**2,end=' ')
        no+=1
    print()

#10
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        if i%2==1:
            print("@",end=' ')
        else:
            print("#",end=' ')
    print()

#11    
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        if j%2==0:
            print("@",end=' ')
        else:
            print("#",end=' ')
    print()

#12
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        if  ((i==1 or j==1 or i==num or j==num )):
            print("#",end=' ')
        else:
            print(" ",end=' ')
    print()

#try
num=int(input("Enter num:"))
for i in range (1,num+1):
    for j in range(1,num+1):
        if i==1 and j==1 or (i==4 and j==1):
             print(" ",end=' ')
        elif  ((i==1 or j==1 or i==num)):
            print("#",end=' ')
        else:
            print(" ",end=' ')
    print()

#try
num=int(input("Enter num:"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 or j==1 or i==3 or j==num:
            print("#",end=' ')
        else:
            print(" ",end=' ')
    print()

#try
num=int(input("enter the number"))
char=65
for i in range(1,num+1):
    for j in range(1,num+1):
        print(chr(char),end=" ")
        char+=1
    print()    

#try
num=int(input("enter the number"))
char=48
for i in range(1,num+1):
    for j in range(1,num+1):
        print(chr(char),end=" ")
        char+=1
    print()    

#06-0
#13
num=int(input("Enter num:"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==(num+1)//2 or j==(num+1)//2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#14
num=int(input("Enter num:"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==j or i+j==(num+1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#15
num=int(input("Enter num:"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==j or i+j==(num+1) or i==(num+1)//2 or j==(num+1)//2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#16
num=int(input("Enter num:"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==j or i+j==(num+1) or i==(num+1)//2 or j==(num+1)//2) or i==1 or j==1 or i==num or j==num:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#17
num=int(input("enter the number"))
char=65
for i in range(1,num+1):
    for j in range(1,num+1):
        print(chr(char),end=" ")
        char+=1
    print()   

#18
num=int(input("enter the number"))
char=97
for i in range(1,num+1):
    for j in range(1,num+1):
        print(chr(char),end=" ")
        char+=1
    print()  

#19
num=int(input("enter the number"))
char=65
char1=97
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 or j==1 or i==num or j==num:
            print(chr(char),end=" ")
            char+=1
        else:
            print(chr(char1),end=' ')
            char1+=1
    print()  

#20
num=int(input("enter the number"))
char=65
digit=49
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 or j==1 or i==num or j==num:
            print(chr(char),end=" ")
            char+=1
        else:
            print(chr(digit),end=' ')
            digit+=1
    print()  


#21
num=int(input("Enter num:"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==num and j!=1 and j!=num 
            or j==num and i!=1 and i!=num
            or i==1 and j!=1 and j!=num
            or j==1 and i!=1 and i!=num):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#22
num=int(input("Enter num:"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==num and j!=1 and j!=num 
            or j==num and i!=1 and i!=num
            or i==1 and j!=1 and j!=num
            or j==1 and i!=1 and i!=num
            or i==j and i!=1 and i!=num
            or i+j==num+1 and j!=1 and j!=num):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#23
num=int(input("Enter num:"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==num and j!=1 and j!=num 
            or j==num and i!=1 and i!=num
            or i==1 and j!=1 and j!=num
            or j==1 and i!=1 and i!=num
            or i==j and i!=1 and i!=num
            or i+j==num+1 and j!=1 and j!=num
            or i==(num+1)//2 or j==(num+1)//2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()


num=5
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i>=j and i+j>=num+1) or (i<=j and i+j<=(num+1)):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print("-------------------------------------------------------------")
print()
num=5
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==(num+1)/2 or (i==1 and j==(num+1)/2) or (i==2 and (j==2 or j==3 or j==4)) or (i==num and j==(num+1)/2) or (i==num-1 and (j==2 or j==3 or j==4)):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()


n=int(input("Enter height of tree:"))
for i in range(n,0,-1):
	print("*"*i)


n=int(input("Enter height of tree:"))
for i in range(1,n+1):
	spaces=n-i
	stars=i*2-1
	print(" "*spaces + "*"*stars)

n=int(input("Enter height of tree:"))
for i in range(1,n+1):
	print("*"*i)


n=int(input("Enter number:"))
for i in range(n,0,-1):
    spaces=n-i
    stars=2*i-1
    print(" "*spaces + "*"*stars)


















