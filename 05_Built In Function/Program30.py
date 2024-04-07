#Concept of __name__="__main__"
import Program29

print("top-level in program30.py")

Program29.func()

if __name__=="__main__":
          print("Program 30 is being run directly")
else:
    print("program 30 is being imported into another module")

