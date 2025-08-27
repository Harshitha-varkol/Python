'''
#1
def area_of_rectangle():
    length=int(input("Enter length:"))
    breadth=int(input("Enter Breadth:"))
    area=length*breadth
    print(area)
for i in range(1,3):
    area_of_rectangle()

#2
def area_of_rectangle(length,breadth):
    area=length*breadth
    print(area)
area_of_rectangle(3,4)

#3
def area_of_square():
    side=int(input("Enter side:"))
    area=side**2
    print(area)
for i in range(1,3):
    area_of_square()

#4
def area_of_square(side):
    area=side**2
    print(area)
for i in range(1,3):
    area_of_square(i)

#5
def area_of_triangle():
    base=int(input("Enter base:"))
    height=int(input("Enter Height:"))
    area=int(1/2*(base*height))
    print(area)
for i in range(1,3):
    area_of_triangle()

#6
def area_of_triangle(base,height):
    area=int(1/2*(base*height))
    print(area)
area_of_triangle(5,10)

#7
def area_of_circle():
    pi=3.142
    radius=int(input("Enter Radius:"))
    area=pi*radius*radius
    print(area)
for i in range(1,3):
    area_of_circle()

#8
def area_of_circle(radius):
    pi=3.142
    area=pi*radius*radius
    print(area)
for i in range(1,3):
    area_of_circle(i)

#9
def area_of_trapezoid():
    base1=int(input("Enter Base1:"))
    base2=int(input("Enter Base2:"))
    ver_height=int(input("Enter Vertical Height:"))
    area=1/2*(base1+base2)*ver_height
    print(area)
for i in range(1,3):
    area_of_trapezoid()

#10
def area_of_trapezoid(base1,base2,ver_height):
    area=1/2*(base1+base2)*ver_height
    print(area)
area_of_trapezoid(12,13,14)

#11
def area_of_ellipse():
    pi=3.142
    rad1=int(input("Enter Radius of major axis:"))
    rad2=int(input("Enter Radius of minor axis:"))
    area=pi*rad1*rad2
    print(area)
for i in range(1,3):
    area_of_ellipse()

#12
def area_of_ellipse(rad1,rad2):
    pi=3.142
    area=pi*rad1*rad2
    print(area)
area_of_ellipse(8,4)

13
#Surface Area Of Rectangular Prism
def s_area_rectangular_prism():
    length=int(input("Enter length:"))
    width=int(input("Enter width:"))
    height=int(input("Enter height:"))
    area=2*(length*width + height*length + height*width)
    print(area)
s_area_rectangular_prism()

#14
def s_area_rectangular_prism(length,width,height):
    area=2*(length*width + height*length + height*width)
    print(area)
s_area_rectangular_prism(12,12,12)

15
def s_area_of_cone():
    pi=3.142
    radius=int(input("Enter radius:"))
    slant_height=int(input("Enter slant_height:"))
    area=pi*radius*(radius+slant_height)
    print(area)
s_area_of_cone()

#16
def s_area_of_cone(radius,slant_height):
    pi=3.142
    area=pi*radius*(radius+slant_height)
    print(area)
s_area_of_cone(12,3)

17
def s_area_of_cylinder():
    pi=3.142
    radius=int(input("Enter radius:"))
    height=int(input("Enter height:"))
    area=2*pi*radius*(radius+height)
    print(area)
s_area_of_cylinder()

#18
def s_area_of_cylinder(radius,height):
    pi=3.142
    area=2*pi*radius*(radius+height)
    print(area)
s_area_of_cylinder(12,18)

19
def area_of_sphere():
     pi=3.142
     radius=int(input("Enter Radius:"))
     area=4*pi*radius*radius
     print(area)
area_of_sphere()

#20
def area_of_sphere(radius):
     pi=3.142
     area=4*pi*radius*radius
     print(area)
area_of_sphere(12)

21
def area_of_kite():
    pi=3.142
    d_length1=int(input("Enter Diagonal 1 length:"))
    d_length2=int(input("Enter Diagonal 2 length:"))
    area=0.5*d_length1*d_length2
    print(area)
area_of_kite()

#22
def area_of_kite(d_length1,d_length2):
    pi=3.142
    area=0.5*d_length1*d_length2
    print(area)
area_of_kite(12,12)

#23
def area_of_polygon():
    pi=3.142r 
    perimeter=int(input("Enter perimeter:"))
    apothem=int(input("Enter apothem:"))
    area=0.5*perimeter*apothem
    print(area)
area_of_polygon()

#24
def area_of_polygon(perimeter,apothem):
    pi=3.142
    area=0.5*perimeter*apothem
    print(area)
area_of_polygon(12,13)



def area_of_rectangle():
        length=int(input("Enter length:"))
        breadth=int(input("Enter Breadth:"))
        area=length*breadth
        print(area)

def area_of_square():
    side=int(input("Enter side:"))
    area=side**2
    print(area)

def area_of_triangle():
    base=int(input("Enter base:"))
    height=int(input("Enter Height:"))
    area=int(1/2*(base*height))
    print(area)

def area_of_circle():
    pi=3.142
    radius=int(input("Enter Radius:"))
    area=pi*radius*radius
    print(area)

def area_of_trapezoid():
    base1=int(input("Enter Base1:"))
    base2=int(input("Enter Base2:"))
    ver_height=int(input("Enter Vertical Height:"))
    area=1/2*(base1+base2)*ver_height
    print(area)

def area_of_ellipse():
    pi=3.142
    rad1=int(input("Enter Radius of major axis:"))
    rad2=int(input("Enter Radius of minor axis:"))
    area=pi*rad1*rad2
    print(area)

def s_area_rectangular_prism():
    length=int(input("Enter length:"))
    width=int(input("Enter width:"))
    height=int(input("Enter height:"))
    area=2*(length*width + height*length + height*width)
    print(area)

def s_area_of_cone():
    pi=3.142
    radius=int(input("Enter radius:"))
    slant_height=int(input("Enter slant_height:"))
    area=pi*radius*(radius+slant_height)
    print(area)

def s_area_of_cylinder():
    pi=3.142
    radius=int(input("Enter radius:"))
    height=int(input("Enter height:"))
    area=2*pi*radius*(radius+height)
    print(area)

def area_of_sphere():
     pi=3.142
     radius=int(input("Enter Radius:"))
     area=4*pi*radius*radius
     print(area)

def area_of_kite():
    d_length1=int(input("Enter Diagonal 1 length:"))
    d_length2=int(input("Enter Diagonal 2 length:"))
    area=0.5*d_length1*d_length2
    print(area)

def area_of_polygon():
    perimeter=int(input("Enter perimeter:"))
    apothem=int(input("Enter apothem:"))
    area=0.5*perimeter*apothem
    print(area)

while True:
    print("Enter 1 to find area of rectangle")
    print("Enter 2 to find area of square")
    print("Enter 3 to find area of triangle")
    print("Enter 4 to find area of circle")
    print("Enter 5 to find area of trapezoid")
    print("Enter 6 to find area of ellipse")
    print("Enter 7 to find surface area of rectangular prism")
    print("Enter 8 to find surface area of cone")
    print("Enter 9 to find surface area of cylinder")
    print("Enter 10 to find area of sphere")
    print("Enter 11 to find area of kite")
    print("Enter 12 to find area of regular polygon")
    num=int(input("Enter number:"))
    if num==1:
        area_of_rectangle()
    elif num==2:
        area_of_square()
    elif num==3:
        area_of_triangle()
    elif num==4:
        area_of_circle()
    elif num==5:
        area_of_trapezoid()
    elif num==6:
        area_of_ellipse()
    elif num==7:
        s_area_rectangular_prism()
    elif num==8:
        s_area_of_cone()
    elif num==9:
        s_area_of_cylinder()
    elif num==10:
        area_of_sphere()
    elif num==11:
        area_of_kite()
    elif num==12:
        area_of_polygon()
    else:
        print("Invalid Input ")
    n=int(input("Enter 1 to repeat 2 to terminate "))
    if(n==1):
        continue
    else:
        break
print("THANKYOU")

#functions with return statement

def spy(no,sum=0,pro=1):
    while no>0:
        rem=no%10
        sum+=rem
        pro*=rem
        no//=10
    return sum,pro
no=int(input("Enter num:"))
sum,pro=spy(no)
print(sum)
print(pro)
if sum==pro:
    print("Spy number")
else:
    print("Not a spy number")

def palindrome(no,rev=0):
    while no>0:
        rev=rev*10+(no%10)
        no//=10
    return rev
no=int(input("Enter num:"))
if palindrome(no)==no:
    print("Palindrome")
else:
    print("Not a palindrome")

def sum(a,b):
    return a+b
print(sum(4,5))


def sub(a,b,c):
    return a-b-c
print(sub(9,8,1))

def sub(a,b,c):
    return a-b-c
print(sub(9,8,))

def sum(a,b):
    print(a+b)
sum(a=30,b=20)

def sum(a,b):
    print(a+b)
sum(b=20,a=20)


#using multiple functions in one program

print("Armstrong numbers")
def count(num,count=0):
    while num>0:
        count+=1
        num//=10
    return count
def armstrong(num):
    num1=num
    sum=0
    digit_count=count(num)
    while num1>0:
        rem1=num1%10
        pow=1
        for i in range(1,digit_count+1):
            pow*=rem1
        sum+=pow
        num1//=10
    return sum
def is_armstrong(num):
    sum=armstrong(num)
    if sum==num:
        return "YES"
    else:
        return "NO"
num=int(input("Enter num:"))
res=is_armstrong(num)
print(res)

print("PALINDROME NUMBER")
def rev(num,rev=0):
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev
def is_palindrome(num):
    if rev(num)==num:
        return "YES"
    else:
        return "NO"
num=int(input("Enter num:"))
res=is_palindrome(num)
print(res)

#RECURSION

print("A-Z")
def char(ascii):
    if 65<=ascii<=90:
        print(chr(ascii),end=' ')
        char(ascii+1)
char(65)

print("a-z")
def char(ascii):
    if 97<=ascii<=122:
        print(chr(ascii),end=' ')
        char(ascii+1)
char(97)

print("ODD NUMBERS from 1 to 100")
def odd_num(no):
    if no%2==1 and no<=100:
        print(no,end=' ')
    odd_num(no+1)
odd_num(1)

print("FACTORIAL")
def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*(factorial(num-1))
num=int(input("Enter num:"))
print(factorial(num))

print("PRIME NUMBERS")
def prime_numbers(num):
    count=0
    if num>100:
        return
    for j in range(1,num+1):
        if num%j==0:
            count+=1
    if count==2:
        print(num)
    prime_numbers(num+1)
prime_numbers(1)




def count(num,count=0):
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return count
def prime_numbers(num):
    count1=count(num)
    if num>100:
        return
    if count==2:
        print(num, "is prime")
    else:
        print(num, "is not prime")
num=int(input("Enter num"))
prime_numbers(num)

#PRIME NUMBERS USING RECURSION
def count_factors(n, i=1, count=0):
    if i > n:
        return count
    if n % i == 0:
        count += 1
    return count_factors(n, i + 1, count)
def is_prime(n):
    if n <= 1:
        return False
    return count_factors(n) == 2
n = int(input("Enter a number: "))
if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")

#PRIME NUMBERS USING RECURSION

def is_prime(num,i):
    if i==1:
        return 1
    elif num%i==0:
        return 0
    return is_prime(num,i-1)
num=int(input("Enter num:"))
is_prime1=is_prime(num,num-1)
if is_prime1==1:
    print("PRIME NUM")
else:
    print("NOT PRIME")

#PRINT FIRST HALF OR LAST HALF OF THE NUMBER using FUNCTIONS
def count(num,count=0):
    while num>0:
        rem=num%10
        count+=1
        num//=10
    return count
def first_half(num):
    count1=count(num)
    half=count1//2
    div=10**half
    return num//div
def second_half(num):
    count1=count(num)
    if count1%2==1:
        count1+=1
    half=count1//2
    div=10**half
    return num%div
b1=True
while b1:
    no=int(input("enter num:"))
    print("Enter 1 to get first half")
    print("Enter 2 to get second half")
    user_input=int(input("Enter num:"))
    if user_input==1:
          first_half=print(first_half(no))
    elif user_input==2:
         second_half=print(second_half(no))
    else:
        print("invalid input")
    print("Do you wanna try again?")
    print("Enter yes to contine or stop to terminate")
    user_input1=input("Enter your choice:")
    if user_input1=="yes":
         b1=True
    elif user_input1=="stop":
         b1=False         
print("THANKYOU")
'''
