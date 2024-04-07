# Exception Handling - try, except

import sys
randomlist=['a',0,2]
for entry in randomlist:
    try:
        print("The entry is :", entry)
        r=1/int(entry)
    except:
        print("Error occcured and try again.Error Message is :", sys.exc_info()[0])
print("The reciprocal of",  entry, " is :", r)


