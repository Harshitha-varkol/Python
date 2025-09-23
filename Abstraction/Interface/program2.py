from abc import*
class V(ABC):
    @abstractmethod
    def v_n(self):
        pass
    @abstractmethod
    def v_c(self):
        pass
    @abstractmethod
    def v_p(self):
        pass

class Car(V):
    def __init__(self,vn,vc,vp):
        self.vn=vn
        self.vc=vc
        self.vp=vp
    
    def v_n(self):
        print(self.vn)
    
    def v_c(self):
        print(self.vc)

    def v_p(self):
        print(self.vp)

class Bike(V):
    def __init__(self,vn,vc,vp):
        self.vn=vn
        self.vc=vc
        self.vp=vp
    
    def v_n(self):
        print(self.vn)
    
    def v_c(self):
        print(self.vc)

    def v_p(self):
        print(self.vp)

class Bus(V):
    def __init__(self,vn,vc,vp):
        self.vn=vn
        self.vc=vc
        self.vp=vp
    
    def v_n(self):
        print(self.vn)
    
    def v_c(self):
        print(self.vc)

    def v_p(self):
        print(self.vp)
    
class Main:
    def main(self,info):
        info.v_n()
        info.v_c()
        info.v_p()

m=Main()
m.main(Car("Swift","Black",800000))
print("--"*10)
m.main(Bike("Pulser","Black",500000))
print("--"*10)
m.main(Bus("Tata","Red",1000000))