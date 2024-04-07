#Flow Control Statements

#break
print("Using Break Statement....")
for i in ['foo','bar','baz','qux']:
    if 'b' in i:
        break
    print("The Value is  :",i)
for j in ['book','note','pen','pencil']:
    if j== 'pen':
        break
    else:
        print(j,'done')
#continue
print("Using Continue Statement....")
for k in ['foo','bar','baz','qux']:
    if 'b' in k:
        continue
    print(i)
#pass
samplelist=[1,2,3,4,5]
for i in samplelist:
    pass
print("Code runs without any error")
