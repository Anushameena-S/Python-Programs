#Lambda Function

ans=(lambda z:z*4)
print(ans(7))

samplelist=[1,2,3,4,5]

#Lambda with Map
op1=list(map(lambda num:num**2,samplelist))
print("Output of Map Function is using lambda  :", op1)

#Lambda with Filter
op2=list(filter(lambda num:num%2==0,samplelist))
print("Output of Filter Function is using lambda:", op2)

#Lambda with Reduce
from functools import reduce
op3=reduce(lambda x,y:x*y,samplelist)
print("The output after performing reduce function with lambda is  :",op3)
