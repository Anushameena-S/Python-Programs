# Multilevel Inheritance
#Lower level classes can inherit functions from the upper level classes

class Animal:
    def eat(self):
        print("Eating....")
class Dog(Animal):
    def bark(self):
        print("Barking....")
class Puppy(Dog):
    def weep(self):
        print("Weeping...")
d=Puppy()
d.eat()
d.bark()
d.weep()
