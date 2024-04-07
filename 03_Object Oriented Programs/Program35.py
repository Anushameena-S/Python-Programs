#OOPS Concept- Variable Scope
# In this program a is global variable and b is local variable
a=90
class First:
    b=20
    def div(self):
        c=a/10
        print("The output of dividing a and 10 are :", c)
objfir=First()
objfir.div()
print("The value of a is ", a)
print("The value of b is :",objfir.b)
