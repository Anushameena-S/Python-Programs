#Get File name, mode,seek and tell the position of file

newfile=open("changedname.txt",'r')

print("The name of the file is :", newfile.name)
print("The name of the file is :",newfile.mode)

newfile.seek(100)
print(newfile.read(20))
print("The position of file is :", newfile.tell())
