#Exception Handling - try, finally with File Operation
import sys
try:
    f=open("test.txt", "r")
    try:
        f.read()
    finally:
        f.close()
except:
    print("The file does not exist")

