#Attributes - User-Defined
#Private, Public and Protected
#private atribute inside class can be accessed only if use constructors

class Sample():
    def __init__(self):
        self.__pri="I am private"
        self._pro="I am protected"
        self.pub="I am public"
obj4=Sample()
print("Private varaible :", obj4._Sample__pri)
print("Protected varaible :", obj4._pro)
print("Public varaible :", obj4.pub)
        

