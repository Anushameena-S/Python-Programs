#Default, keyword and Variable Length Arguments
#Default
def func1(a,b,c,d=8):
    return a*d+b*c
print(func1(3,2,1))
print(func1(1,5,2,3))

#Keyword
print(func1(c=6,b=5,d=1,a=2))

#Variable length
def func2(dept,*members):
    print("The Department is  :", dept)
    print("The members are :",members)
func2("maths","aarthi","bala","catherine","divya")
