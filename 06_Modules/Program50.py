#Random Module

import random

num=random.randrange(100)
print("The randrange with one arg gives value :",num)

ran=random.randrange(0,100,20)
print("The randrange with three arg with steps of 20 :",ran)

inte=random.randint(0,30)
print("The randint gives :", inte)

print("The object for Current internal state of the generator is :", random.getstate)

print("The random.uniform gives value :", random.uniform(6,2))

