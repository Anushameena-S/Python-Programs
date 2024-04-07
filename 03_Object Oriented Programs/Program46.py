#Getter and Setter Methods

class College:
    def __init__(self,course_Name):
        self.course_Name=course_Name
    def setcourse_Name(self,course_Name):
        self.course_Name=course_Name.upper()
    def getcourse_Name(self):
        return(self.course_Name)

col=College("Maths")
print("The first course name is :",col.getcourse_Name())

col.setcourse_Name("Computer Science")
print("The next course name is :", col.getcourse_Name())
