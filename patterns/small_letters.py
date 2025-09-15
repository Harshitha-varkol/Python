
#a
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==((num+1)/2)-1 and j<=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2 or i==num-1 and j<=(num+1)/2 or j==1 and i>=((num+1)/2)+1 and i!=num or i==((num+1)/2)+1 and j<=(num+1)/2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#b
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1 or i==num and j<=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2: 
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#c
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==num+1/2 and j<=(num+1)/2 or j==1 and i>=(num+1)/2 or i==num and j<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2: 
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#d
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==(num+1)/2 or i==num and j<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2 or j==1 and i>=(num+1)/2  : 
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#e
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 and j<=(num+1)/2 or j==1 and i<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2 or j==(num+1)//2 and i<=(num+1)//3 or i==(num+1)//3 and j<=(num+1)//2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#f
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==(num+1)/2 or i==(num+1)/2 and j>=(num+1)/3 or i==1 and j>=(num+1)/2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#g
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==(num+1)/2 or i==num and j<=(num+1)/2 or i==1 and j<=(num+1)/2 or j==1 and i<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2 or i==(num-1) and j==1:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#h
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1 or (i==(num+1)/2 and j<=(num+1)/2) or (j==(num+1)/2 and i>=(num+1)/2):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#i
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==(num+1)/2 and i>=(num+1)/2 or (j==(num+1)/2 and i==((num+1)/2)-2):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#j
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if (j==(num+1)/2 and i>=(num+1)/3) or i==num and j<=(num+1)/2 or (j==(num+1)/2 and i==2):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#k
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==(num+1)/2 or (i+j==num+3 and j>((num+1)/2) and i>=((num+1)/2)-4) or (i==j and j>((num+1)/2)+1 and i>((num+1)/2)-1):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#l
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#m
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==(num+1)/2 and j!=1 and j!=(num+1)/2 and j!=num) or (j==1 and i!=(num+1)/2 ) and i>=(num+1)/2 or (j==num and i!=(num+1)/2) and i>=(num+1)/2 or (j==(num+1)/2 and i!=(num+1)/2) and i>=(num+1)/2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#n
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==(num+1)/2 and j<=(num+1)/2 and j!=1 and j!=(num+1)/2) or (j==(num+1)/2 and i!=(num+1)/2 and i>=(num+1)/2) or (j==1 and i>=(num+1)/2 and i!=(num+1)/2):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#o
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==(num+1)/2 and j<=(num+1)/2 and j!=1 and j!=(num+1)/2) or (j==1 and i>=(num+1)/2 and i!=(num+1)/2 and i!=num) or (i==num and j<=(num+1)/2 and j!=1 and j!=(num+1)/2) or (j==(num+1)/2 and i>=(num+1)/2 and i!=(num+1)/2 and i!=num):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#p
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1 or i==1 and j<=(num+1)/2 or j==(num+1)/2 and i<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#q
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 and j<=(num+1)/2 or j==1 and i<=(num+1)/2 or j==(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2 or i==num-1 and j==((num+1)/2)+1 or i==num-2 and j==(num+1)/2+2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#r
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==(num+1)/2 and i>=((num+1)/3)-1 or i+j==num+1 and j>=(num+1)/2 and i!=1 and i!=2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#s
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==(num+1)/2 and j<=(num+1)/2 or j==1 and i>=(num+1)/2 and i<=(num+1)/2+2 or i==(num+1)/2+2 and j<=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2+2 and i<=num or i==num and j<=(num+1)/2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#t
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==(num+1)/2 or i==num and j>=(num+1)/2 and j<=(num-2) or i==(num+1)/2 and j>=(num+1)/3 and j<=(num-3):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#u
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1 and i>=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2 or i==num and j<=(num+1)/2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#v
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1 and i<=(num+1)/3 or j==(num+1)/2 and i<=(num+1)/3 or j==((num+1)//3)-1 and i==((num+1)//3)+1 or i==((num+1)/2)-1 and j==((num+1)/2)-1 or j==((num+1)/2)-2 and i==((num+1)/2):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#w
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1 and i>=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2 or i==num-2 and j==(num+1)//3 or i==num-1 and j==((num+1)//3)-1 or i==num-1 and j==((num+1)//3)+1:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#X
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i+j==num+1 and i>=(num+1)/2 or i==(num+1)/2 and j==1 or i==((num+1)/2)+1 and j==((num+1)//3)-1 or i==((num+1)/2)+3 and j==((num+1)//3)+1 or i==num and j==(num+1)/2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#y
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1 and i<(num+1)/2 or i==((num+1)/2)-1 and j<=((num+1)/2)-1 or j==(num+1)/2 or i==num and j<=(num+1)/2 or i==num-1 and j==1:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

#z
print()
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==(num+1)/2 and j<=(num+1)/2 or i+j==num+1 and j<=(num+1)/2 or i==num and j<=(num+1)/2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()