
#0
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if (j==num-1 and i!=1 and i!=num) or (j==2 and i!=1 and i!=num) or (i==1 and j!=2 and j!=1 and j!=num and j!=num-1) or (i==num and j!=2 and j!=1 and j!=(num-1) and j!=num):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#1
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==num or j==(num+1)/2 or i==2 and j==((num+1)/2)-1 or i==3 and j==((num+1)/2)-2 or i==4 and j==((num+1)/2)-3 or i==(num+1)/2 and j==1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#2
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 and j!=num or j==num and i!=1 and i<(num+1)/2 or i==num or j==1 and i>(num+1)/2 and j!=(num+1)/2 or i==(num+1)/2 and j!=1 and j!=num:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#3
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 and j!=num or i==num and j!=num or j==num and i!=1 and i!=(num+1)/2 and i!=num or i==(num+1)/2 and j!=num:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#4
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i+j==num+1 and j!=num and j!=1 or i==num-1 and j!=1 or j==num-1 and i!=1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#5
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 or j==1 and i<=(num+1)/2 and i!=1 or j==num and i!=num and i!=1 and i>(num+1)/2 or i==(num+1)/2 and j!=num or i==num and j!=num:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#6
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 and j!=1 or j==1 and i!=1 and i!=num or j==num and i!=num and i>(num+1)/2 or i==(num+1)/2 and j!=num or i==num and j!=1 and j!=num:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#7
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i+j==num+1 or i==1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#8
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if (j==num-1 and i!=1 and i!=num and i!=(num+1)/2) or (j==2 and i!=1 and i!=num and i!=(num+1)/2) or (i==1 and j!=2 and j!=1 and j!=num and j!=num-1) or (i==num and j!=2 and j!=1 and j!=(num-1) and j!=num) or i==(num+1)/2 and j!=num and j!=(num-1) and j!=1 and j!=2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#9
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if (j==num and i!=1 and i!=num) or (i==1 and j!=num and j!=1) or (i==num and j!=num) or (i==(num+1)/2 and j!=1) or (j==1 and i!=1 and i<=(num+1)/2 and i!=(num+1)/2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()


