# TYPE CASTING ALL OTHER DATA TYPES INTO INT
float1=123.23
int1=int(float1)
bool1=True
int2=int(bool1)
complex1=10+1j
c1=int(complex1.real)
c2=int(complex1.imag)
string1="1234567890"
int3=int(string1)
print(int1)
print(type(int1))
print(bool1)
print(type(bool1))
print(c1)
print(type(c1))
print(c2)
print(type(c2))
print(string1)
print(type(string1))

# TYPE CASTING ALL OTHER DATA TYPES INTO FLOAT

int4=123
float2=float(int1)
print(float2)
print(type(float2))
bool2=False
float3=float(bool2)
print(float3)
print(type(float3))
complex2=10+20j
float4=float(complex1.real)
print(float4)
print(type(float4))
float41=float(complex1.imag)
print(float41)
print(type(float41))
string1="123.12"
float5=float(string1)
print(float5)
print(type(float5))

#TYPE CASTING OTHER DATA TYPES INTO BOOL

int2=18
bool2=bool(int2)
print(bool2)
print(type(bool2))
float5=1234.34
bool3=bool(float5)
print(bool3)
print(type(bool3))
complex2=100+30j
bool4=bool(complex2)
print(bool4)
print(type(bool4))
string2="KANE"
bool5=bool(string2)
print(bool5)
print(type(bool5))

#TYPE CASTING OTHER DATA TYPES INTO STRING

int3=1199
string3=str(int3)
print(string3)
print(type(string3))
bool6=True
string4=str(bool6)
print(string4)
print(type(string4))
float6=123.45
string5=str(float6)
print(string5)
print(type(string5))
complex4=10+20j
string6=str(complex4)
print(string6)
print(type(string6))

#TYPE CASTING OTHER DATA TYPES INTO COMPLEX

int6=1234
complexa=complex(int6)
print(complexa)
print(type(complexa))
floata=123.45
complexb=complex(floata)
print(complexb)
print(type(complexb))
boola=True
complexd=complex(boola)
print(complexd)
print(type(complexd))
stringa="KANE"
complexc=complex(stringa)
print(complexc)
print(type(complexc))