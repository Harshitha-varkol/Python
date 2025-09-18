class Battery:
    def __init__(self,name,capacity):
        self.name=name
        self.capacity=capacity
    def getbatteryinfo(self):
        print("Battery Name:",self.name)
        print("Capacity:",self.capacity)

class Sim:
    def __init__(self,name,contactno):
        self.name=name
        self.contactno=contactno
    def getsiminfo(self):
        print("Sim name:",self.name)
        print("Contact no:",self.contactno)

class Mobile:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    def getmobileinfo(self):
        print("Name:",self.name)
        print("Color:",self.color)
        print("Price:",self.price)
        b=Battery("XYZ","5000mah")
        b.getbatteryinfo()
    def insertsim(self,sim):
        sim.getsiminfo()

m=Mobile("VIVO","PURPLE",29999)
m.getmobileinfo()
m.insertsim(Sim("Airtel",9876547897))

