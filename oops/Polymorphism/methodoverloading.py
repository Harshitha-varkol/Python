class Calci:
    def add(self):
        print("No argument method")
    def add(self,a1):
        print("one argument method",a1)
    def add(self,a1,a2):
        print("two argument method",a1,a2)
c=Calci()
c.add(12,18)


#achieving method overloading by using (*args) variable length arguments

class Calci:
    def add(self,*args):
        for i in args:
            print(i)
c=Calci()
c.add(1,2.25,"a","arha")