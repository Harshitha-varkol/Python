from abc import *
class RBI(ABC):

    def __init__(self,name,no_of_emp,no_of_accounts):
        self.name=name
        self.no_of_emp=no_of_emp
        self.no_of_accounts=no_of_accounts

    @abstractmethod
    def rate_of_interest(self):
        pass

    @abstractmethod
    def min_balance(self):
        pass

class SBI(RBI):
    def __init__(self, name, no_of_emp, no_of_accounts,no_of_branches):
        super().__init__(name, no_of_emp, no_of_accounts)
        self.no_of_branches=no_of_branches
    
    def rate_of_interest(self):
        print(self.name," ",self.no_of_emp," ",self.no_of_accounts," ",self.no_of_branches )
        print("Rate of interest is 6%")
    
    def min_balance(self):
        print("No minimum balance required")

class ICICI(RBI):
    def __init__(self, name, no_of_emp, no_of_accounts,location):
        super().__init__(name, no_of_emp, no_of_accounts)
        self.location=location
    
    def rate_of_interest(self):
        print(self.name," ",self.no_of_emp," ",self.no_of_accounts," ",self.location)
        print("Rate of interest is 10%")
    
    def min_balance(self):
        print("Minimum balance should be 1000rs ")

class HDFC(RBI):
    def __init__(self, name, no_of_emp, no_of_accounts,no_of_customers):
        super().__init__(name, no_of_emp, no_of_accounts)
        self.no_of_customers=no_of_customers

    def rate_of_interest(self): 
        print(self.name," ",self.no_of_emp," ",self.no_of_accounts," ",self.no_of_customers)
        print("Rate of interest is 20%")
    
    def min_balance(self):
        print("Minimum balance should be 2000rs ")


class Main:

    def ansim(self,obj):
        obj.rate_of_interest()
        obj.min_balance()

m=Main()
m.ansim(SBI("SBI",30,10000,40))
print("--"*10)
m.ansim(ICICI("ICICI",40,20000,"PUNJAGUTTA"))
print("--"*10)
m.ansim(HDFC("HDFC",50,30000,400))
    