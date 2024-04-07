# Constructors and Destructors

class Test:
    def __init__(self):
        print("I am constructor")
    def __del__(self):
        print("I am destructor")
ob5 = Test()
del ob5
