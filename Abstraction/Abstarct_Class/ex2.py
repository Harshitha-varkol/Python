from abc import*
class Mobile(ABC):
    
    @abstractmethod
    def demo(self):
        pass

    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

class Demo(Mobile):
    def demo(self):
        print("Demo function")
d=Demo("VIVO","RED",29000)
d.demo()

from abc import*
class Mobile(ABC):
    def __init__(self,name,col,price):
        self.name=name
        self.col=col
        self.price=price
    @abstractmethod
    def getmobileinfo(self):
        pass

class Mobileuser(Mobile):
    def __init__(self, name, col, price,u_name):
        super().__init__(name, col, price)
        self.u_name=u_name
    
    def getmobileinfo(self):
        print(self.u_name)
        print(self.name,self.col,self.price)
d=Mobileuser("vivo","red",29999,"kane")
d.getmobileinfo()