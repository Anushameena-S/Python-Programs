# OS Module
import os
import os.path
#While specifing directory, program accepts
#only forward slash and use single quotes

print("The current directory is :", os.getcwd())
print("The new directory is :", os.mkdir("C:/newtest"))
print(os.chdir("C:/test"))
print("The current directory is :", os.getcwd()) 

print("The removed directory is :", os.rmdir("C:/newtest"))

print("The os name is :", os.name)
print("The os environment is :", os.environ)
print("The os login is :",os.getlogin())
print("The process id is :", os.getppid)

print("The joined path is :", os.path.join('C:/Users/Akshaya/Documents/Anusha','C:/Users/Akshaya/Documents/SAMPLE'))
                   
print("The complete path of the file is :", os.path.abspath('07_Modules'))
print("The standard path is :", os.path.normpath('Users/Documents/Anusha/Python Programs/07_Modules'))
print("The directory split is :",os.path.split('C:/Users/Akshaya/Documents/Anusha/Python Programs/07_Modules'))
print("The path exists or not :",os.path.exists('C:/Users/Akshaya/Documents/Anusha/Python Programs/07_Modules'))
print("The path exists or not :",os.path.exists('C:/Users/Akshaya/Documents/Anusha/Python Programs/08_Modules'))
print("Is it a directory or not :", os.path.isdir('C:/Users/Akshaya/Documents/Anusha'))
print("Is it a directory or not :", os.path.isdir('C:/Users/Akshaya/Documents/Anusha/test'))

print("The files present in the path are :\n")
for i in os.walk('C:/Users/Akshaya/Documents/Anusha/Python Programs/07_Modules'):
    print(i)
 
