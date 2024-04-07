#Function with arguments
def func1(name,age):
    print("Name of the person is  :",name)
    print("Age of the Person is  :", age)
func1("Ram", 31)

def func2(m1,m2,m3,m4,m5):
    total = m1+m2+m3+m4+m5
    percnt= (total*100)/500
    return percnt
stu_percnt=func2(54,78,65,89,97)
print("Student got percentage of " , stu_percnt)
