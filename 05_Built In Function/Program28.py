#Verify Built-in functions
#abs()
a=-5
print("The absolute value is :",abs(a))

#all()
b=[True,'fds',4,5]
print("all of b is :", all(b))
c=[True,False]
print("all of c is :", all(c))
d=[5,6,None]
print("all of d is :", all(d))
e=[3,4,0]
print("all of e is :", all(e))

#any()
print("any of b is :", any(b))
print("any of c is :", any(c))
print("any of d is :", any(d))
print("any of e is :", any(e))
f=any([False,0,None])
print("any of f is :", f)

#bin()
h=3
print("The binary value of h is :",bin(h))

#bool()
i=bool(True)
print("i is :", i)
j=bool(0)
print("j is :", j)

#chr()
k=chr(244)
print("k is :",k)
l=chr(257)
print("l is :",l)

#enumerate()
grocery=["bread","butter","milk"]
sampleenum=enumerate(grocery)
print("The type of sample is :", type(sampleenum))
print("The contents of sample are :", list(sampleenum))
sampleenum=enumerate(grocery,10)
print("Now The contents of sample are :", list(sampleenum))

#eval()
m=eval('5+7')
print("m is :",m)

#globals()
print("globals() gives :", globals())

#id(variablename)
print("id of variable h is ", id(h))

#int()
print("int function returns :",int('214'))

#reversed()
for n in reversed([2,3,4,5,6]):
    print("n is :",n)

#sum()
z=[1,9,5,2]
print("The sum gives :", sum(z))


