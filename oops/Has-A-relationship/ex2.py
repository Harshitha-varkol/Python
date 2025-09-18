class Engine:
    def __init__(self,horsepower):
        self.horsepower=horsepower
    def getcarinfo(self):
        print(self.horsepower)
    def start(self):
        print("Starts The Car")

class Wheels:
    def __init__(self,count):
        self.count=count
    def getcarinfo(self):
        print(self.count)
    def rotate(self):
        print("Wheels Rotate")

class Car:
    def __init__(self,name):
        self.name=name
    def getcarinfo(self):
        print(self.name)
        e=Engine(123)
        e.getcarinfo()
        e.start()
        w=Wheels(4)
        w.getcarinfo()
        w.rotate()
    def drive(self):
        print("Drivers drive the car")

c=Car("SWIFT")
c.getcarinfo()
c.drive()