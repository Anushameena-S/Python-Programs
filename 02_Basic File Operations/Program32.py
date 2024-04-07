#read file,rename file name and delete file
import os

#r - reads file, r+ - both read and write file
newfile=open("samplefile.txt",'r')

#Reads only 5 character
#print(newfile.read(5))

#Reads entire file
print(newfile.read())

#newfile.write("Try to write in read mode")

newfile1.close()

#rename
#os.rename("samplefile.txt","changedname.txt")
#os.rename("changedname.txt","samplefile.txt")

#Remove file
#os.remove("Lambda Expressions.txt")

#readline()-Same like read() but slower and inefficient
#print(newfile.readline(15))



