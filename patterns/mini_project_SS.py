num = 9
name = input("ENTER NAME:")
for i in range(1, num + 1): 
    for ch in name:
        for j in range(1, num + 1):
            if ch == 'A':
                if (j == 1 and i != 1) or (j == num and i != 1) or (i == 1 and j != 1 and j != num) or i == (num + 1) // 2:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif ch == 'B':
                if (i == 1 and j != num) or (i == num and j != num) or (i == (num + 1) // 2 and j != num) or (j == num and i != 1 and i != num and i != (num + 1) // 2) or j == 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif ch == 'C':
                if (i == 1 and j != 1) or (i == num and j != 1) or (j == 1 and i != 1 and i != num):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif ch=='C':
                if (i==1 and j!=1) or (i==num and j!=1) or (j==1 and i!=1 and i!=num): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='D':
                if (i==1 and j!=num) or (i==num and j!=num) or j==1 or (j==num and i!=1 and i!=num): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='E':
                if (j==1 and i!=1 and i!=num) or (i==1 and j!=1) or (i==num and j!=1) or i==(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='F':
                if (i==1 and j!=1) or (j==1 and i!=1) or i==(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='G':
                if i==1 or i==num or j==1 or (j==num and i>(num+1)/2) or (i==(num+1)/2 and j>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='H':
                if j==1 or j==num or i==(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='I':
                if i==1 or i==num or j==(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='J':
                if i==1 or (i==num and j<=(num+1)/2) or j==(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='K':
                if j==(num+1)/2 or (i+j==num+1 and i<=(num+1)/2) or (i==j and i>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='L':
                if j==1 or i==num: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='M':
                if j==1 or j==num or (i==j and i<=(num+1)/2) or (i+j==num+1 and j>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='N':
                if j==1 or j==num or i==j: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='O':
                if (j==1 and i!=1 and i!=num) or (j==num and i!=1 and i!=num) or (i==1 and j!=1 and j!=num) or (i==num and j!=1 and j!=num): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='P':
                if (j==1) or (j==num and i<(num+1)/2 and i!=1 and i!=(num+1)/2) or (i==1 and j!=num) or (i==(num+1)/2 and j!=num): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='Q':
                if (j==1 and i!=num and i!=1 and i!=num-1) or (j==num-1 and i!=num and i!=1 and i!=num-1) or (i==1 and j!=num and j!=1 and j!=num-1) or (i==num-1 and j!=num and j!=1) or (i==num and j==num and j!=num) or (i==j and i>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='R':
                if j==(num+1)/2 or (j==num and i<=(num+1)/2) or (i==1 and j>=(num+1)/2) or (i==(num+1)/2 and j>=(num+1)/2) or (i==j and i>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='S':
                if j==1 and i<=(num+1)/2 or i==1 or i==(num+1)/2 or i==num or (j==num and i>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='T':
                if i==1 or j==(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='U':
                if (j==1 and i!=num) or (i==num and j!=1 and j!=num) or (j==num and i!=num): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='V':
                if i==j and i<=(num+1)/2 or i+j==num+1 and i<=(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='W':
                if j==1 or j==num or (i==j and i>=(num+1)/2) or (i+j==num+1 and i>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='X':
                if i==j or i+j==num+1: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='Y':
                if (i==j and i<=(num+1)/2) or (i+j==num+1 and i<=(num+1)/2) or (j==(num+1)/2 and i>=(num+1)/2): 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='Z':
                if i==1 or i+j==num+1 or i==num: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='a':
                if i==((num+1)/2)-1 and j<=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2 or i==num-1 and j<=(num+1)/2 or j==1 and i>=((num+1)/2)+1 and i!=num or i==((num+1)/2)+1 and j<=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            elif ch=='b':
                if j==1 or i==num and j<=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='c':
                if i==num+1/2 and j<=(num+1)/2 or j==1 and i>=(num+1)/2 or i==num and j<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='d':
                if j==(num+1)/2 or i==num and j<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2 or j==1 and i>=(num+1)/2  : 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='e':
                if i==1 and j<=(num+1)/2 or j==1 and i<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2 or j==(num+1)//2 and i<=(num+1)//3 or i==(num+1)//3 and j<=(num+1)//2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='f':
                if j==(num+1)/2 or i==(num+1)/2 and j>=(num+1)/3 or i==1 and j>=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='g':
                if j==(num+1)/2 or i==num and j<=(num+1)/2 or i==1 and j<=(num+1)/2 or j==1 and i<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2 or i==(num-1) and j==1:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='h':
                if j==1 or (i==(num+1)/2 and j<=(num+1)/2) or (j==(num+1)/2 and i>=(num+1)/2):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='i':
                if j==(num+1)/2 and i>=(num+1)/2 or (j==(num+1)/2 and i==((num+1)/2)-2):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='j':
                if (j==(num+1)/2 and i>=(num+1)/3) or i==num and j<=(num+1)/2 or (j==(num+1)/2 and i==2):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='k':
                if j==(num+1)/2 or (i+j==num+3 and j>((num+1)/2) and i>=((num+1)/2)-4) or (i==j and j>((num+1)/2)+1 and i>((num+1)/2)-1):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='l':
                if j==1:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='m':
                if (i==(num+1)/2 and j!=1 and j!=(num+1)/2 and j!=num) or (j==1 and i!=(num+1)/2 ) and i>=(num+1)/2 or (j==num and i!=(num+1)/2) and i>=(num+1)/2 or (j==(num+1)/2 and i!=(num+1)/2) and i>=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='n':
                if (i==(num+1)/2 and j<=(num+1)/2 and j!=1 and j!=(num+1)/2) or (j==(num+1)/2 and i!=(num+1)/2 and i>=(num+1)/2) or (j==1 and i>=(num+1)/2 and i!=(num+1)/2):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='o':
                if (i==(num+1)/2 and j<=(num+1)/2 and j!=1 and j!=(num+1)/2) or (j==1 and i>=(num+1)/2 and i!=(num+1)/2 and i!=num) or (i==num and j<=(num+1)/2 and j!=1 and j!=(num+1)/2) or (j==(num+1)/2 and i>=(num+1)/2 and i!=(num+1)/2 and i!=num):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='p':
                if j==1 or i==1 and j<=(num+1)/2 or j==(num+1)/2 and i<=(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='q':
                if i==1 and j<=(num+1)/2 or j==1 and i<=(num+1)/2 or j==(num+1)/2 or i==(num+1)/2 and j<=(num+1)/2 or i==num-1 and j==((num+1)/2)+1 or i==num-2 and j==(num+1)/2+2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='r':
                if j==(num+1)/2 and i>=((num+1)/3)-1 or i+j==num+1 and j>=(num+1)/2 and i!=1 and i!=2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='s':
                if i==(num+1)/2 and j<=(num+1)/2 or j==1 and i>=(num+1)/2 and i<=(num+1)/2+2 or i==(num+1)/2+2 and j<=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2+2 and i<=num or i==num and j<=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='t':
                if j==(num+1)/2 or i==num and j>=(num+1)/2 and j<=(num-2) or i==(num+1)/2 and j>=(num+1)/3 and j<=(num-3):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='u':
                if j==1 and i>=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2 or i==num and j<=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='v':
                if j==1 and i<=(num+1)/3 or j==(num+1)/2 and i<=(num+1)/3 or j==((num+1)//3)-1 and i==((num+1)//3)+1 or i==((num+1)/2)-1 and j==((num+1)/2)-1 or j==((num+1)/2)-2 and i==((num+1)/2):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='w':
                if j==1 and i>=(num+1)/2 or j==(num+1)/2 and i>=(num+1)/2 or i==num-2 and j==(num+1)//3 or i==num-1 and j==((num+1)//3)-1 or i==num-1 and j==((num+1)//3)+1:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='x':
                if i+j==num+1 and i>=(num+1)/2 or i==(num+1)/2 and j==1 or i==((num+1)/2)+1 and j==((num+1)//3)-1 or i==((num+1)/2)+3 and j==((num+1)//3)+1 or i==num and j==(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='y':
                if j==1 and i<(num+1)/2 or i==((num+1)/2)-1 and j<=((num+1)/2)-1 or j==(num+1)/2 or i==num and j<=(num+1)/2 or i==num-1 and j==1:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='z':
                if i==(num+1)/2 and j<=(num+1)/2 or i+j==num+1 and j<=(num+1)/2 or i==num and j<=(num+1)/2:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            elif ch=='0':
                if (j==num-1 and i!=1 and i!=num) or (j==2 and i!=1 and i!=num) or (i==1 and j!=2 and j!=1 and j!=num and j!=num-1) or (i==num and j!=2 and j!=1 and j!=(num-1) and j!=num):
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            elif ch=='1':
                if i==num or j==(num+1)/2 or i==2 and j==((num+1)/2)-1 or i==3 and j==((num+1)/2)-2 or i==4 and j==((num+1)/2)-3 or i==(num+1)/2 and j==1:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            elif ch=='2':
                if i==1 and j!=num or j==num and i!=1 and i<(num+1)/2 or i==num or j==1 and i>(num+1)/2 and j!=(num+1)/2 or i==(num+1)/2 and j!=1 and j!=num:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            elif ch=='3':
                if i==1 and j!=num or i==num and j!=num or j==num and i!=1 and i!=(num+1)/2 and i!=num or i==(num+1)/2 and j!=num:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            elif ch=='4':
                if i+j==num+1 and j!=num and j!=1 or i==num-1 and j!=1 or j==num-1 and i!=1:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            elif ch=='5':
                if i==1 or j==1 and i<=(num+1)/2 and i!=1 or j==num and i!=num and i!=1 and i>(num+1)/2 or i==(num+1)/2 and j!=num or i==num and j!=num:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            elif ch=='6':
                if i==1 and j!=1 or j==1 and i!=1 and i!=num or j==num and i!=num and i>(num+1)/2 or i==(num+1)/2 and j!=num or i==num and j!=1 and j!=num:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            elif ch=='7':
                if i+j==num+1 or i==1:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            elif ch=='8':
                if (j==num-1 and i!=1 and i!=num and i!=(num+1)/2) or (j==2 and i!=1 and i!=num and i!=(num+1)/2) or (i==1 and j!=2 and j!=1 and j!=num and j!=num-1) or (i==num and j!=2 and j!=1 and j!=(num-1) and j!=num) or i==(num+1)/2 and j!=num and j!=(num-1) and j!=1 and j!=2:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            elif ch=='9':
                if (j==num and i!=1 and i!=num) or (i==1 and j!=num and j!=1) or (i==num and j!=num) or (i==(num+1)/2 and j!=1) or (j==1 and i!=1 and i<=(num+1)/2 and i!=(num+1)/2):
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print(" ", end="") 
    print()

    