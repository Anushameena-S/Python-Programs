#OOPS - Attributes - Built-In

class Employee:
    '''
    Employee information
    '''
    empcount=1000

print("The information of this program is :", Employee.__dict__)
print("The comment of this program is :", Employee.__doc__)
print("The name of this program is :", Employee.__name__)
print("The module of this program is :", Employee.__module__)
print("The bases of this program is :", Employee.__bases__)
