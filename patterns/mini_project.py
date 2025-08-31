num=9
name=input("Enter your name:")
for i in name:
    if i=='A':
        print( )
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (j==1 and i!=1 )or (j==num and i!=1) or (i==1 and j!=1 and j!=num) or i==(num+1)/2 :
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    
    elif i=='B':
        print( )
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (i==1 and j!=num) or (i==num and j!=num) or (i==(num+1)/2 and j!=num) or (j==num and i!=(num+1)/2 and i!=1 and i!=num) or j==1: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    
    elif i=='C':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (i==1 and j!=1) or (i==num and j!=1) or (j==1 and i!=1 and i!=num): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    
    elif i=='D':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (i==1 and j!=num) or (i==num and j!=num) or j==1 or (j==num and i!=1 and i!=num): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='E':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (j==1 and i!=1 and i!=num) or (i==1 and j!=1) or (i==num and j!=1) or i==(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='F':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (i==1 and j!=1) or (j==1 and i!=1) or i==(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='G':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==1 or i==num or j==1 or (j==num and i>(num+1)/2) or (i==(num+1)/2 and j>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='H':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1 or j==num or i==(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='I':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==1 or i==num or j==(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='J':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==1 or (i==num and j<=(num+1)/2) or j==(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='K':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==(num+1)/2 or (i+j==num+1 and i<=(num+1)/2) or (i==j and i>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='L':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1 or i==num: 
                    print("*",end=' ')
            else:
                    print(" ",end=" ")
            print()
    elif i=='M':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1 or j==num or (i==j and i<=(num+1)/2) or (i+j==num+1 and j>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='N':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1 or j==num or i==j: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='O':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (j==1 and i!=1 and i!=num) or (j==num and i!=1 and i!=num) or (i==1 and j!=1 and j!=num) or (i==num and j!=1 and j!=num): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='P':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (j==1) or (j==num and i<(num+1)/2 and i!=1 and i!=(num+1)/2) or (i==1 and j!=num) or (i==(num+1)/2 and j!=num): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='Q':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (j==1 and i!=num and i!=1 and i!=num-1) or (j==num-1 and i!=num and i!=1 and i!=num-1) or (i==1 and j!=num and j!=1 and j!=num-1) or (i==num-1 and j!=num and j!=1) or (i==num and j==num and j!=num) or (i==j and i>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='R':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==(num+1)/2 or (j==num and i<=(num+1)/2) or (i==1 and j>=(num+1)/2) or (i==(num+1)/2 and j>=(num+1)/2) or (i==j and i>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='S':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1 and i<=(num+1)/2 or i==1 or i==(num+1)/2 or i==num or (j==num and i>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='T':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==1 or j==(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='U':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (j==1 and i!=num) or (i==num and j!=1 and j!=num) or (j==num and i!=num): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='V':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==j and i<=(num+1)/2 or i+j==num+1 and i<=(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='W':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1 or j==num or (i==j and i>=(num+1)/2) or (i+j==num+1 and i>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='X':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==j or i+j==num+1: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='Y':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (i==j and i<=(num+1)/2) or (i+j==num+1 and i<=(num+1)/2) or (j==(num+1)/2 and i>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='Z':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==1 or i+j==num+1 or i==num: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    
    elif i=='a':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==((num+1)/2)-1 and j<=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2 or i==num-1 and j<=(num+1)/2 or j==1 and i>=((num+1)/2)+1 and i!=num or i==((num+1)/2)+1 and j<=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
    elif i=='b':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1 or i==num and j<=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='c':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==num+1/2 and j<=(num+1)/2 or j==1 and i>=(num+1)/2 or i==num and j<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='d':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==(num+1)/2 or i==num and j<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2 or j==1 and i>=(num+1)/2  : 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='e':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==1 and j<=(num+1)/2 or j==1 and i<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2 or j==(num+1)//2 and i<=(num+1)//3 or i==(num+1)//3 and j<=(num+1)//2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='f':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==(num+1)/2 or i==(num+1)/2 and j>=(num+1)/3 or i==1 and j>=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='g':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==(num+1)/2 or i==num and j<=(num+1)/2 or i==1 and j<=(num+1)/2 or j==1 and i<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2 or i==(num-1) and j==1:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='h':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1 or (i==(num+1)/2 and j<=(num+1)/2) or (j==(num+1)/2 and i>=(num+1)/2):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='i':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==(num+1)/2 and i>=(num+1)/2 or (j==(num+1)/2 and i==((num+1)/2)-2):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='j':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (j==(num+1)/2 and i>=(num+1)/3) or i==num and j<=(num+1)/2 or (j==(num+1)/2 and i==2):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='k':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==(num+1)/2 or (i+j==num+3 and j>((num+1)/2) and i>=((num+1)/2)-4) or (i==j and j>((num+1)/2)+1 and i>((num+1)/2)-1):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='l':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='m':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (i==(num+1)/2 and j!=1 and j!=(num+1)/2 and j!=num) or (j==1 and i!=(num+1)/2 ) and i>=(num+1)/2 or (j==num and i!=(num+1)/2) and i>=(num+1)/2 or (j==(num+1)/2 and i!=(num+1)/2) and i>=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='n':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (i==(num+1)/2 and j<=(num+1)/2 and j!=1 and j!=(num+1)/2) or (j==(num+1)/2 and i!=(num+1)/2 and i>=(num+1)/2) or (j==1 and i>=(num+1)/2 and i!=(num+1)/2):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='o':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (i==(num+1)/2 and j<=(num+1)/2 and j!=1 and j!=(num+1)/2) or (j==1 and i>=(num+1)/2 and i!=(num+1)/2 and i!=num) or (i==num and j<=(num+1)/2 and j!=1 and j!=(num+1)/2) or (j==(num+1)/2 and i>=(num+1)/2 and i!=(num+1)/2 and i!=num):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='p':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1 or i==1 and j<=(num+1)/2 or j==(num+1)/2 and i<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='q':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==1 and j<=(num+1)/2 or j==1 and i<=(num+1)/2 or j==(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2 or i==num-1 and j==((num+1)/2)+1 or i==num-2 and j==(num+1)/2+2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='r':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==(num+1)/2 and i>=((num+1)/3)-1 or i+j==num+1 and j>=(num+1)/2 and i!=1 and i!=2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='s':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==(num+1)/2 and j<=(num+1)/2 or j==1 and i>=(num+1)/2 and i<=(num+1)/2+2 or i==(num+1)/2+2 and j<=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2+2 and i<=num or i==num and j<=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='t':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==(num+1)/2 or i==num and j>=(num+1)/2 and j<=(num-2) or i==(num+1)/2 and j>=(num+1)/3 and j<=(num-3):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='u':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1 and i>=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2 or i==num and j<=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='v':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1 and i<=(num+1)/3 or j==(num+1)/2 and i<=(num+1)/3 or j==((num+1)//3)-1 and i==((num+1)//3)+1 or i==((num+1)/2)-1 and j==((num+1)/2)-1 or j==((num+1)/2)-2 and i==((num+1)/2):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='w':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1 and i>=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2 or i==num-2 and j==(num+1)//3 or i==num-1 and j==((num+1)//3)-1 or i==num-1 and j==((num+1)//3)+1:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='x':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i+j==num+1 and i>=(num+1)/2 or i==(num+1)/2 and j==1 or i==((num+1)/2)+1 and j==((num+1)//3)-1 or i==((num+1)/2)+3 and j==((num+1)//3)+1 or i==num and j==(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='y':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j==1 and i<(num+1)/2 or i==((num+1)/2)-1 and j<=((num+1)/2)-1 or j==(num+1)/2 or i==num and j<=(num+1)/2 or i==num-1 and j==1:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='z':
        print()
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==(num+1)/2 and j<=(num+1)/2 or i+j==num+1 and j<=(num+1)/2 or i==num and j<=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    elif i=='0':
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (j==num-1 and i!=1 and i!=num) or (j==2 and i!=1 and i!=num) or (i==1 and j!=2 and j!=1 and j!=num and j!=num-1) or (i==num and j!=2 and j!=1 and j!=(num-1) and j!=num):
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
    elif i=='1':
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==num or j==(num+1)/2 or i==2 and j==((num+1)/2)-1 or i==3 and j==((num+1)/2)-2 or i==4 and j==((num+1)/2)-3 or i==(num+1)/2 and j==1:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
    elif i=='2':
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==1 and j!=num or j==num and i!=1 and i<(num+1)/2 or i==num or j==1 and i>(num+1)/2 and j!=(num+1)/2 or i==(num+1)/2 and j!=1 and j!=num:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
    elif i=='3':
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==1 and j!=num or i==num and j!=num or j==num and i!=1 and i!=(num+1)/2 and i!=num or i==(num+1)/2 and j!=num:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
    elif i=='4':
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i+j==num+1 and j!=num and j!=1 or i==num-1 and j!=1 or j==num-1 and i!=1:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
    elif i=='5':
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==1 or j==1 and i<=(num+1)/2 and i!=1 or j==num and i!=num and i!=1 and i>(num+1)/2 or i==(num+1)/2 and j!=num or i==num and j!=num:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
    elif i=='6':
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i==1 and j!=1 or j==1 and i!=1 and i!=num or j==num and i!=num and i>(num+1)/2 or i==(num+1)/2 and j!=num or i==num and j!=1 and j!=num:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
    elif i=='7':
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i+j==num+1 or i==1:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
    elif i=='8':
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (j==num-1 and i!=1 and i!=num and i!=(num+1)/2) or (j==2 and i!=1 and i!=num and i!=(num+1)/2) or (i==1 and j!=2 and j!=1 and j!=num and j!=num-1) or (i==num and j!=2 and j!=1 and j!=(num-1) and j!=num) or i==(num+1)/2 and j!=num and j!=(num-1) and j!=1 and j!=2:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
    elif i=='9':
        for i in range(1,num+1):
            for j in range(1,num+1):
                if (j==num and i!=1 and i!=num) or (i==1 and j!=num and j!=1) or (i==num and j!=num) or (i==(num+1)/2 and j!=1) or (j==1 and i!=1 and i<=(num+1)/2 and i!=(num+1)/2):
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
    
    else:
        print("SPECIAL CHARACTERS ARE NOT ALLOWED")