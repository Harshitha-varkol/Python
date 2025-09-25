def outer():
    print("outer function")
    def inner():
        print("inner function")
    inner()
outer()

# def outer():
#     print("Outer function")
#     def inner():
#         print("inner function")
#     inner()
#     outer()
# outer() 

def even(no):
    if no%2==0:
        return True
l1=[22,34,33,44]
l2=list(filter(even,l1))
print(l2)