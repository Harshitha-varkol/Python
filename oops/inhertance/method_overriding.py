'''
class Paytm:    
    def send(self):
        print("Send Money")
class User(Paytm):
    def send(self):
        super().send()
        print("Sending money to mom")
p1=User()
p1.send()
print("---"*9)
class Book:
    book_name="IT ENDS WITH US"
    def __init__(self,author,price):
        self.author=author
        self.price=price
    def getbookinfo(self):
        print("Author of the book:",self.author)
        print("Price of the book:",self.price)
    @classmethod
    def bookname(cls):
        print(Book.book_name)
    @staticmethod
    def feedback():
         print("GOOD BOOK")
class Book1(Book):
    bookname1="IT STARTS WITH US"
    def __init__(self, author, price,pages):
        self.pages=pages
        super().bookname()
        super().__init__(author, price)
    def getbookinfo(self):
        super().getbookinfo()
        print("Number of pages in the book:",self.pages)    
    @classmethod
    def bookname(cls):
        super().bookname()
        print(Book1.bookname1)
    @staticmethod
    def feedback(): #here static methods cannot be inherited
        print("AWESOME BOOK")
        super().feedback()
b=Book1("COLLEEN HOOVER",500,600)
b.getbookinfo()
b.bookname()
b.feedback()


#accessing private and protected members in child class
class Vehicle:
    def __init__(self,brand,wheels,year):
        self.__brand=brand
        self._wheels=wheels
        self._year=year
    def getvehicleinfo(self):
        print("The brand of vehicle is:",self.__brand)
        print("No.of Wheels:",self._wheels)

class Car(Vehicle):
    def __init__(self, brand, wheels,year,model):
        super().__init__(brand, wheels,year)
        self.model=model
    def getcarinfo(self):
        super().getvehicleinfo()
        print("The model of car is:",self.model)
        print("The year of manufacturing is:",self._year)
c1=Car("Maruti suzuki",4,2007,"Swift")
c1.getcarinfo()

print("--------------------------------------------------------------------------")

#Multi-Level Inheritance
class Windows10:
    def __init__(self,name,yol):
        self.name=name
        self.yol=yol
    def windowsinfo(self):
        print("Name of OS:",self.name)
        print("Year of launch:",self.yol)
class Windows11(Windows10):
    def __init__(self, name, yol,performance):
        super().__init__(name, yol)
        self.performance=performance
    def windowsinfo(self):
        super().windowsinfo()
        print("Performance of OS:",self.performance)
class Windows12(Windows11):
    def __init__(self, name, yol, performance,security):
        super().__init__(name, yol, performance)
        self.security=security
    def windowsinfo(self):
        super().windowsinfo()
        print("The security is:",self.security)
w1=Windows12("Windows 10",2018,"Good","Windows Defender")
w1.windowsinfo()

'''
