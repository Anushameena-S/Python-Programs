#Range Function
# aruguments in range(): initial value, number-1,interval.
# first parameter should be always lesser than the second parameter
# otherwise, range function will return blank values
#To print the range values, we have to either
#use For Loop or convert it into List/Tuple

#1. Use For Loop
print("In i Loop.....")
for i in range(4):
  print(i)
print("In j Loop.....")
for j in range(5,10,1):
    print(j)
print("In k Loop.....")
for k in range(5,20,3):
    print(k)
print("In l Loop.....")
for l in range(5,10):
    print(l)
print("In m Loop.....")
for m in range(-5,5):
    print(m)
print("In n Loop.....")
for n in range(5,-5):
    print(n)
print("In o Loop.....")
for o in range(5,-5,-1):
    print(o)
print("In p Loop.....")
for p in range(10,3):
    print(p)

#2. convert it into List/Tuple
c=list(range(10,5,-1))
print("Range Converted to List and Printed  :",c)
