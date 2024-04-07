#Sequence Operation on Set
#Set
x={1,4,3,5,2,4,3,6}
y={5,4,6,7}
z={5,4,6,7,9}
n={2,3,10}
print("The value of set x are :", x)

#Add
x.add(10)
print("After addition :",x)

#Update
x.update([22,33],{555,777,888})
print("After update :", x)

#Remove
x.remove(4)
print("After removal :", x)

#Discard
x.remove(555)
print("After discard :", x)

#Pop - pops an element - starts from 1st element in the set
x.pop()
print("After pop :", x)

#Clear
print("Y values are:",y)
y.clear()
print("Y values are:",y)

#Union
print("The union of x and z are :", x|z)

#Intersection
print("The intersection of x and z are :", x&z)

#Difference
print("The difference of x and z are :", x-z)

#Issuperset
print("is x super set of n", x.issuperset(n))

#Issubset
print("is n sub set of x", n.issubset(x))

a={1,2,3,4,5}
b={4,5,6,7,8}

#Union, Intersection and Difference

print("After union :",a.union(b))

print("After intersection :",a.intersection(b) )

print("After difference :",b.difference(a))

