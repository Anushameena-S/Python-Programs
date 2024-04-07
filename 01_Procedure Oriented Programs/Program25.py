#Sequence Operation on List
lis1=['a','b','c','d','e','m','n']
lis2=[1,2,5,3,8,6]
lis3=[(1,2,3),{'aaa':234,'bbb':345,'ccc':456}]

#List with tuple and dictionary
print("The tuple in lis3 is :", lis3[0])
print("The dictionary in lis3 is :", lis3[1])

#Concatenation
print("The output of concatenation is :", lis1+lis2)

#Repetition
print("The output of repitition is  :", lis1*2)

#Membership Testing
print("is x in lis1 :", 'x' in lis1)
print("is x not in lis1 :", 'x' not in lis1)
print("is d in lis1 :", 'd' in lis1)

#Slicing
print("The part 1 of lis1 is :", lis1[0:5])
print("The part 2 of lis2 is :", lis1[5:7])

#Indexing
print("The fourth element of lis2 is :",lis2[3])

#Length
print("The length of lis1 is :", len(lis1))

#append
lis1.append('x')
print("After append :", lis1)

#extend
lis1.extend(['r','s','t'])
print("After extend :", lis1)

#sorted
print("The sorted lis2 is ", sorted(lis2))

#Reverse
print("The reverse of lis2 is :", lis2[::-1])

#insert
lis2.insert(4,'new')
print("Lis2 after new value insertion is :",lis2)

#type
print("The type of lis1 is :", type(lis1))
print("The type of lis2 is :", type(lis2))

#delete
del(lis1[3])
print("The lis1 values after deletion is :", lis1)

#remove
lis1.remove('x')
print("The lis1 values after removal is :", lis1)

#pop
lis1.pop(3)
print("The lis1 value after pop is :",lis1)

#max
print("The max value of lis1 is :", max(lis1))

#Min
print("The min value of lis1 is :", min(lis1))
