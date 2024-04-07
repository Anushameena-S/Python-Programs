#Sequence Operations on String
str1="verifyr"
str2="program"

#Concatenation
result=str1+str2
print(result)

#Repetition
result2=str1*3
print(result2)

#Membership Testing
print("is a member of str1", 'a' in str1)
print("is a not a member of str1", 'a' not in str1)
print("is o a member of str2", 'o' in str2)

#Slicing
part1=str1[0:3]
part2=str1[3:6]
print("The part 1 of str1 is  :", part1)
print("The part 1 of str1 is  :", part2)


#Indexing
print("The reversed order of str2 is  :", str2[::-1])
print("The third letter in str is :", str2[2])

#Length
print("The length of str1 is  ",len(str1))
print("The length of str2 is  ",len(str2))

#count
c=str2.count('r',0,len(str2))
print("The count of r in str2 is :",c)

#Capitalize
print(str1.capitalize())

#Uppercase
print(str2.upper())

#Maximum of String
print("The max of str1 is :",max(str1))

#Minimum of String
print("The min of str1 is :",min(str1))

#replace
print("r is replaced by R for 1 time  :",str2.replace('r', '--R--',1))

#encode
print(str1.encode('UTF-8','Strict'))

#find
print("The a is found in position:", str1.find('a'))

#index
print("The a is found in position:", str1.index('a'))



