#Method Overriding example 2

class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def getArea(self):
            print(self.length*self.breadth, "is the area of rectangle")
class Square(Rectangle):
    def __init__(self,side):
        self.side=side
        Rectangle.__init__(self,side,side)
    def getArea(self):
        print(self.side*self.side, "is the area of square")

s=Square(4)
r=Rectangle(4,5)
s.getArea()
r.getArea()
    
    
