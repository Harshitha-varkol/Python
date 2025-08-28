'''
#M
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1 or j==num or (i==j and i<=(num+1)/2) or (i+j==num+1 and j>=(num+1)/2): 
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#Y
print( )
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i+j==num+1 or i==j and i<=(num+1)/2) :
            print("|",end=' ')
        else:
            print(" ",end=" ")
    print()

#S
print( )
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==1 and j!=1) or (j==1 and i!=1 and i!=(num+1)/2)and i<=(num+1)/2 or (i==num and j!=num) or (j==num and i!=(num+1)/2 and i!=num) and i>=(num+1)/2 or (i==(num+1)//2 and j!=1 and j!=num):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#T
print( )
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 or j==(num+1)/2 :
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#U
print( )
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if (j==1 and i!=num or j==num and i!=num or i==num and j!=1 and j!=num) :
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()


#D
print( )
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1 or i==1 and j!=num or i==num and j!=num and j!=1 or j==num and i!=1 and i!=num:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#E
print( )
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if (j==1 and i!=1 and i!=num) or (i==1 and j!=1) or (i==num and j!=1) or i==(num+1)/2: 
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#N
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1 or j==num or i==j: 
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#T
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 or j==(num+1)/2: 
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#S
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1 and i<=(num+1)/2 or i==1 or i==(num+1)/2 or i==num or (j==num and i>=(num+1)/2): 
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()


#R
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==(num+1)/2 and i!=1 or (j==num and i<=(num+1)/2 and i!=1 and i!=(num+1)/2) or (i==1 and j>=(num+1)/2 and j!=(num+1)/2 and j!=num) or (i==(num+1)/2 and j>=(num+1)/2 and j!=num) or (i==j and i>=(num+1)/2): 
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()


#R
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==(num+1)/2 or (j==num and i<=(num+1)/2) or (i==1 and j>=(num+1)/2) or (i==(num+1)/2 and j>=(num+1)/2) or (i==j and i>=(num+1)/2): 
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
'''

