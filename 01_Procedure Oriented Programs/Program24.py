#Sequence Operation on Tuple
tup1 =(1,2,3)
tup2=(4,5,6)
tup3=(7,8,9,10,11,12,13,4,1,2,5,54)
tup4=([45,53,23,56],[78,87,98,23],[56,54,34,90])

#Tuple with List
print("The second element in tuple is :", tup4[1])
print("The third number of list in 3rd element in tuple is :", tup4[2][2])

#Concatenation
print("The output of concatenation is :",tup1+tup2)

#Repetition
print("The output of repitition i :", tup2*3)

#Membership Testing
print("is 2 in tup1 :", 2 in tup1)
print("is 5 in tup1 :", 5 in tup1)
print("is 5 not in tup1 :", 5 not in tup1)

#Slicing
print("The part1 of tup3 is :", tup3[0:6])
print("The part2 of tup3 is :", tup3[6:12])

#Indexing
print("The third number in tup3 is :",tup3[2])

#Length
print("The length of tup1 is  :", len(tup1))
print("The length of tup3 is  :", len(tup3))

#Max
print("The max of tup1 is  :", max(tup3))

#Min
print("The max of tup1 is  :", min(tup3))

#Sorted
print("The sorted order of tup3 is  :", sorted(tup3))

#Reversed
print("The reversed order of tup1 is  :",tup3[::-1])

#Delete
del(tup3)
print("The content of tup3 after deletion :", tup3)
