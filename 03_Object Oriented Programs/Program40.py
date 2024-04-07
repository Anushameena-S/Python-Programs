#Single Inheritance

class Base:
    def func1(self):
        print("In class base....")

class Sub(Base):
    def func2(self):
        print("In class sub...")

ob=Sub()
ob.func2()
ob.func1()
