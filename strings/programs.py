print("WAPP TO ACCEPT SOME STRING AND DISPLAY ITS CHARACTERS BY INDEX WISE BOTH POSITIVE AND NEGATIVE INDEX")
str1=input("ENTER A STRING:")
for i in range(0,len(str1)):
    print(str1[i],end="")
print()
for i in range(-1,-(len(str1))-1,-1):
    print(str1[i],end="")

print("WAPP TO REMOVE SPACE IN THE GIVEN SENTENCE")
str1="HII MY NAME IS AKSHITHA"
str2=""
for i in str1:
    if i!=" ":
        str2+=i
print(str2)

print("WAPP TO REMOVE DUPLICATE CHAR IN GIVEN STRING")
str1="VOILAAAAHHHHELLLLOOOOO"
str2=""
for i in str1:
    if i not in str2:
        str2+=i
print(str2)

print("WAPP TO COUNT NUMBER OF SPECIAL CHARACTERS IN GIVEN STRING")
str1="_-Akshu@!:';#"
count=0
for i in str1:
    if not(65<=ord(i)<=90 or 96<=ord(i)<=122 or 48<=ord(i)<=57):
        count+=1
print("NUMBER OF SPECIAL CHARACTERS IN THE STRING IS : ",count)

print("WAPP TO REVERSE EACH WORD IN GIVEN SENTENCE")
input1="HELLO WASTE FELLOW"
l1=input1.split()
print(l1)
for i in l1:
    for j in range(-1,-(len(i))-1,-1):
        print(i[j],end='')
    print()


print("WAPP TO COUNT OCCURENCE OF EACH CHARACTER IN A STRING")
str1="HELLO HELL HOLL HILL"
str2=""
for i in str1:
    count=1
    if i not in str2 and i!=" ":
        str2+=i
for j in str2:
    count=0
    for i in str1:
        if i==j:
            count+=1
    print(j+":",count)