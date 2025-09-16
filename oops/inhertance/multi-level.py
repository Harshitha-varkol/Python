'''
class Iphone14pro:
    def __init__(self,color,price):
        self.color=color
        self.price=price
    def getinfo(self):
        print("Color:",self.color)
        print("Price:",self.price)
    def iphonebehaviour(self):
        print("useful for business purposes")
        print("many features")
class Iphone15pro(Iphone14pro):
    def __init__(self, color, price,cam,storage):
        super().__init__(color, price)
        self.cam=cam
        self.storage=storage
    def getinfo(self):
        super().getinfo()
        print("Cam:",self.cam)
        print("Storage:",self.storage)
    def iphonebehaviour(self):
        super().iphonebehaviour()
        print("Skype calling")
        print("Click high quality images")
class Iphone16pro(Iphone15pro):
    def __init__(self, color, price, cam, storage,battery,ios):
        super().__init__(color, price, cam, storage)
        self.battery=battery
        self.ios=ios
    def getinfo(self):
        super().getinfo()
        print("Battery:",self.battery)
        print("IOS:",self.ios)
    def iphonebehaviour(self):
        super().iphonebehaviour()
        print("Voice Mail")
        print("High security")
i1=Iphone16pro("Black",99000,"48 MP","8 GB","4222 MAH","IOS 18")
print("PROPERTIES:")
i1.getinfo()
print("--"*30)
print("BEHAVIOURS:")
i1.iphonebehaviour()

'''
