#Understand Map,Filter and Reduce
samplelist=[1,2,3,4,5]

def sqfunc(num):
    return num**2

    
def check_even(num):
    return num%2==0

def mul(x,y):
    return x*y

#Map
op1=list(map(sqfunc,samplelist))
print("Output of Map Function is  :", op1)

for m in map(sqfunc,samplelist):
    print("The Values after performing map function is  :", m)

#Filter

op2=list(filter(check_even,samplelist))
print("Output of Filter Function is :", op2)

for n in filter(check_even,samplelist):
    print("The values after applying filter is :", n)

#Reduce
from functools import reduce
op3=reduce(mul,samplelist)
print("The output after performing reduce function is  :",op3)
