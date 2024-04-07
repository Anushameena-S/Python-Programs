#Concept of __name__="__main__"
def func():
    print("func() is program29.py")
print("im program29")
print("top-level in program29.py")

if __name__=="__main__":
          print("Program 29 is being run directly")
else:
    print("program 29 is being imported into another module")
    


