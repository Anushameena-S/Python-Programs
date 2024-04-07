#User Defined Exception

class Error(Exception):
    pass
class ValueSmallError(Error):
    pass
class ValueLargeError(Error):
    pass
num=10
while True:
    try:
        in_num=int(input("Enter a number"))
        if in_num<num:
            raise ValueSmallError
        elif in_num>num:
            raise ValueLargeError
        break
    except ValueSmallError:
        print("The Value is very smaller,try again")
        print()
    except ValueLargeError:
        print("The Value is very larger,try again")
        print()
    
print("You have guessed it correctly")
        
        
