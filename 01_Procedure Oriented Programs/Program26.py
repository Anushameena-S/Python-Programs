#Sequence operation on Dictionary
dic1={'Name': 'aaa','Age':23,'Occupation': 'bbb', 'gender':'f'}
dic2={'x':11,'y':22,'z':33}
dic3={'tup':(5,4,6,3),'lis':[2,3,7,5,45,34]}

#Dictionary with tuple and list
print("The tuple in dictionary is :", dic3.get('tup'))
print("The list in dictionary is :", dic3.get('lis'))

#copy
dic4=dic2.copy()
print("The values in dic4 are :",dic4)

#clear
dic4.clear()
print("The values in dic4 after clearing the values are :",dic4)

#Items
print("The items in dic1 are :", dic1.items())

#Keys
print("The key in dic1 are :", dic1.keys())

#Values
print("The values in dic1 are :", dic1.values())

#length
print("The length of dic2 is :", len(dic2))

#Delete
dic5=dic2.copy()
print("The dic5 values are :", dic5)
del(dic5)
#print("after deletion :", dic5)

#string
print("The str of dic1 is :", str(dic1))

#setdefault
print("The default value set to occupation is :",dic1.setdefault('occupation','ccc'))
print("Now the dic1 values are :", dic1)

#sorted
print("The sorted dic1 key are :", sorted(dic1))
print("The sorted dic2 values are :", sorted(dic2.values()))

#type
print("The type of dic is :", type(dic1))


