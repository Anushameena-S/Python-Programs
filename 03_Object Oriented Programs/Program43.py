#Method overriding example 1

class Parent:
    def myMethod(self):
        print("calling parent method.....")

class Child:
    def myMethod(self):
        print("calling child method....")

c=Child()
c.myMethod()
