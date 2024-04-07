#New file Open, write, Close File and append to a file

#w+ - both write and read file. if file doesn't exist,create new file
#If, file exists, it overwrites the file

newfile=open("samplefile.txt", 'w+')

for i in range(0,10):
    newfile.write("Hello!!!This file is a sample file\n")
    
#print(newfile.read())
 
newfile.close()

#a+ - both append and write
newfile=open("samplefile.txt", 'a+')

for j in range(0,5):
    newfile.write("This is appended line \n")

newfile.close()
  

