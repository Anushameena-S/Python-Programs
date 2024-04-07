#Conditional Statement
#If
a=10
b=20
if a<b:
    print("A is lesser than B")
    
#If….. Else
totalscore = int(input("Enter the Total Score"))
if totalscore > 50:
    print("Student has passed")
else:
    print("Student has failed")
    
#If…elif…elif…else
mark1= int(input("Enter the mark1"))
if mark1 >= 90:
    print("Student has got S grade")
elif mark1 < 90 and mark1 >= 80:
    print("Student has got A grade")
elif mark1 <80 and  mark1 >= 70:
    print("Student has got B grade")
elif mark1<70 and mark1 >= 60:
    print("Student has got C grade")
elif mark1<60 and mark1 >= 50:
    print("Student has got D grade")
else:
    print("Student has failed")

