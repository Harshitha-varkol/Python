'''
class Animal:
    def info(self):
        print("Animals do sounds")
        print("Animals eat other animals")
class Cat(Animal):
    def info(self):
        print("Cat says MEOW")
        print("Cat eats Rat")
class Dog(Animal):
    def info(self):
        print("Dog says BOW BOW")
        print("Dog eats Cats")
class Snake(Animal):
    def info(self):
        print("Snake says HISS HISS")
        print("Snake eats Frogs")
c1=Cat()
d1=Dog()
s1=Snake()
c1.info()
d1.info()
s1.info()
'''
class RBI:
    def __init__(self,no_of_emp,rate_of_interest):
        self.no_of_emp=no_of_emp
        self.rate_of_interest=rate_of_interest
        print("number of employees=",self.no_of_emp)
        print("number of employees=",self.rate_of_interest)
class ICICI(RBI):
    def __init__(self, no_of_emp, rate_of_interest,icic_no_emp,icic_rate_of_interest):
        super().__init__(no_of_emp, rate_of_interest)
        self.icic_no_of_emp=icic_no_emp
        self.icic_rate_of_interest=icic_rate_of_interest
        print("number of employees=",self.icic_no_of_emp)
        print("number of employees=",self.icic_rate_of_interest)
class SBI(RBI):
    def __init__(self, no_of_emp, rate_of_interest,sbi_emp,sbi_roi):
        super().__init__(no_of_emp, rate_of_interest)
        self.sbi_emp=sbi_emp
        self.sbi_roi=sbi_roi
        print("number of employees=",self.sbi_emp)
        print("number of employees=",self.sbi_roi)
class MY(RBI):
    def __init__(self, no_of_emp, rate_of_interest,my_emp,my_roi):
        super().__init__(no_of_emp, rate_of_interest)
        self.my_emp=my_emp
        self.my_roi=my_roi
        print("number of employees=",self.my_emp)
        print("number of employees=",self.my_roi)
b1=ICICI(20,5,30,5)
b2=SBI(30,6,40,6)
b3=MY(20,5,50,60)



print("--"*20)

class RBI:
    def __init__(self,no_of_emp,rate_of_interest):
        self.no_of_emp=no_of_emp
        self.rate_of_interest=rate_of_interest
        print("number of employees=",self.no_of_emp)
        print("number of employees=",self.rate_of_interest)
class ICICI(RBI):
    def __init__(self, no_of_emp, rate_of_interest):
        print("ICICI BANK")
        super().__init__(no_of_emp, rate_of_interest)
class SBI(RBI):
    def __init__(self, no_of_emp, rate_of_interest):
        print("SBI BANK")
        super().__init__(no_of_emp, rate_of_interest)
class MY(RBI):
    def __init__(self, no_of_emp, rate_of_interest):
        print("MY BANK")
        super().__init__(no_of_emp, rate_of_interest)
b1=ICICI(20,5)
b2=SBI(40,6)
b3=MY(50,7)