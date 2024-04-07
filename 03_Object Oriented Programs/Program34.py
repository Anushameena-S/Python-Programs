#OOPS Concept - Class, Method, Attribute and Object creation

class Vehicle():
    def func(self):
        print("This is first program in oops concept")
    def func1(self, vehtype, vehcolor):
        self.vehtype =vehtype
        self.vehcolor=vehcolor
        print("The vehicle type and color are :\n", vehtype, "\n",vehcolor)
        
obj1=Vehicle()
obj1.func()
obj1.func1("Car", "Grey")
obj2= Vehicle()
obj2.func1("Bus","Red")
    
