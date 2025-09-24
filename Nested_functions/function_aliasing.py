def demo():
    print("Demo function")
demo()
ref=demo
print(ref) #gives address of demo function
print(id(ref)) #address of ref variable
ref()