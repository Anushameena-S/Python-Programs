#Program to understand the local and global variable
a=10
def add():
    global d
    b=20
    c=a+b
    print("A is  :",a)
    print("B is  :",b)
    print("C is  :",c)
add()
d=50
print("D is  :",d)
