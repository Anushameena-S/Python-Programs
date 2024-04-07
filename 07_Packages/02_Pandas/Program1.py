#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import numpy as np
seriessamp=pd.Series([4,3,2,1])
arr=np.array([90,28,55,47,43])
print(arr)
print(type(arr))
series1=pd.Series(arr)
print(seriessamp)
print(type(seriessamp))
print(series1)
print(series1[0:2])



# In[20]:


import pandas as pd
dict1={'a':1,'b':5,'c':7,'d':4}
list1=[56,43,23,21]
series2=pd.Series(dict1)
series3=pd.Series(list1)
print(series2)
print(series3)


# In[38]:


import pandas as pd
list2=[34,23,56,78,98]
dict2=[{'a':2,'b':8},{'a':7,'b':2},{'a':65,'b':87,'c':34}]
arr2=np.array([[3,2,1,5],[2,3,7,8],[1,8,9,2]])
table1=pd.DataFrame(list2)
table2=pd.DataFrame(dict2)
print(table1)
print(table2)
table3=pd.DataFrame(dict2,index=['row1','row2','row3'])
print(table3)
table4=pd.DataFrame(list2,index=['r1','r2','r3','r4','r5'])
print(table4)
table5=pd.DataFrame(arr2)
print(table5)



# In[86]:


import pandas as pd
import numpy as np
series1=pd.Series([45,43,67],index=['maths','chemistry','physics'])
series2=pd.Series([64,56,98],index=['maths','chemistry','physics'])
table3=pd.DataFrame({
    'Jim':series1,
    'Dwight':series2
})
print(table3)
table3['pam']=pd.Series([34,87,91],index=['maths','chemistry','physics'])
print(table3)
jim_series=table3.pop('Jim')
print(jim_series)
del table3['Dwight']
print(table3)
print(table3.loc['maths'])
print(table3.iloc[2])
series3=pd.Series([30,80,98,90],index=['maths','chemistry','physics','english'])
table4=pd.DataFrame({'Moni':series3})
table5=table3.append(table4,ignore_index=True)
print(table5)


# In[88]:


import pandas as pd
import numpy as np
series1=pd.Series([45,43,67],index=['maths','chemistry','physics'])
series2=pd.Series([64,56,98],index=['maths','chemistry','physics'])
table3=pd.DataFrame({
    'Jim':series1,
    'Dwight':series2
})
#print(table3)
table3['pam']=pd.Series([34,87,91],index=['maths','chemistry','physics'])
#print(table3)
table3.to_csv("C:/Users/Akshaya/Documents/Anusha/Python Programs/08_Packages/02_Pandas/test.csv")
table6=pd.read_csv("C:/Users/Akshaya/Documents/Anusha/Python Programs/08_Packages/02_Pandas/test.csv")
print(table6)


# In[90]:


import pandas as pd
import numpy as np
series1=pd.Series([45,43,67],index=['maths','chemistry','physics'])
series2=pd.Series([64,56,98],index=['maths','chemistry','physics'])
table3=pd.DataFrame({
    'Jim':series1,
    'Dwight':series2
})
#print(table3)
table3['pam']=pd.Series([34,87,91],index=['maths','chemistry','physics'])
#print(table3)
table3.to_excel("C:/Users/Akshaya/Documents/Anusha/Python Programs/08_Packages/02_Pandas/testexcel.xlsx")
sheet=pd.read_excel("C:/Users/Akshaya/Documents/Anusha/Python Programs/08_Packages/02_Pandas/testexcel.xlsx")
print(sheet)

