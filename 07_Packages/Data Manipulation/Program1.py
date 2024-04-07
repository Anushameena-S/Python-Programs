#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
df=pd.Series(np.arange(0,51,2))
print("The dimension is :",df.ndim)
print("The start,stop and step values are :",df.axes)
print("The values are :", df.values)
print("The first 5 values are :\n", df.head())
print("The last 5 values are :\n", df.tail())
print("The first 10 values are :\n", df.head(10))
print("The first 10 values are :\n",df.tail(10))


# In[22]:


import numpy as np
import pandas as pd
df=pd.Series(np.arange(0,51,2))
df1=pd.DataFrame({'First Set':df,'Second Set':pd.Series(np.arange(51,100,2))})
#print(df1)
print(df1.axes)
print(df1.values)
print(df1.head())
print(df1.tail())
print(df1.head(10))
print(df1.tail(10))
print(df1.ndim)
print(df1.shape)
print(type(df1))


# In[31]:


import numpy as np
import pandas as pd
df3=pd.DataFrame({'Odd':pd.Series(np.arange(1,100,2)),'Even':pd.Series(np.arange(0,100,2))})
#print(df3['Odd'])
#print(df3['Even'])
print("The sum of odd and even numbers are :\n", df3.sum())
print("The Standard deviation of odd and even numbers are :\n", df3.std())
print("The statistics of the odd numbers are :\n", df3['Odd'].describe())
print("The statistics of the even numbers are :\n", df3['Even'].describe())
#print("The sum of odd numbers are :",df3['Odd'].sum())
#print("The sum of even numbers are :", df3['Even'].sum())


# In[33]:


import numpy as np
import pandas as pd
df4=pd.DataFrame(np.random.rand(5,4),columns=['Column1','Column2','Column3','Column4'])
for key,value in df4.iteritems():
    print("Key :\n" , key)
    print("Value :\n", value,type(value))


# In[34]:


import numpy as np
import pandas as pd
df4=pd.DataFrame(np.random.rand(5,4),columns=['Column1','Column2','Column3','Column4'])
for key,value in df4.iterrows():
    print("Key :\n",key)
    print("Value :\n",value)
    print("Dimension :\n", value.ndim)


# In[37]:


import numpy as np
import pandas as pd
df4=pd.DataFrame(np.random.rand(5,4),columns=['Column1','Column2','Column3','Column4'])
print("The tuple of each row is :\n")
for row in df4.itertuples():
    print(row)
    print("The type of row is :\n",type(row))


# In[65]:


import pandas as pd
world_cup={'Team':['WestIndies','WestIndies','India','Australia','Pakistan','Srilanka','Australia','Australia','India','Australia','Australia'],
          'Rank':[7,7,2,1,6,4,1,1,1,2,1],
          'Year':[1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015]}
df5=pd.DataFrame(world_cup)
print(df5)
print(df5.groupby(['Team']).groups)
print(df5.groupby(['Team','Rank']).groups)
print("\nThe grouping is done below :\n")
for name,group in df5.groupby('Team'):
    print("The name of the country is :",name)
    print("The grouping based of the country is :\n",group)
    print("\n")
    print("The ranks of the country are :\n",group['Rank'])
    print("\n")
grouped=df5.groupby('Team')
print("The group of india is :\n", grouped.get_group('India'))


# In[66]:


import numpy as np
import pandas as pd
df3=pd.DataFrame({'Odd':pd.Series(np.arange(1,100,2)),'Even':pd.Series(np.arange(0,100,2))})
print(df3.groupby('Odd').groups)


# In[4]:


import pandas as pd
world_champions={'Team':['India','Australia','WestIndies','Pakistan','Srilanka'],
                'ICCRank':[2,3,7,8,4],'Year':[2011,2015,1979,1922,1996],'Points':[874,787,753,673,855]}
chokers={'Team':['SouthAfrica','Newzland','Zimbabwe'], 'ICCRank':[1,5,9],'Points':[895,764,656]}
df1=pd.DataFrame(world_champions)
df2=pd.DataFrame(chokers)
print(pd.concat([df1,df2]))


# In[17]:


import pandas as pd
a=pd.DataFrame({'key':['k0','k1','k2','k3','k4'],
               'A':['A0','A1','A2','A3','A4'],
               'B':['B0','B1','B2','B3','B4']})
b=pd.DataFrame({'key':['k0','k1','k3','k5','k6'],
               'c':['C0','C1','C2','C3','C5'],
               'D':['D0','D1','D2','D3','D5']})
#print(pd.concat([a,b]))
#print(a.append(b))
print(b.append(a))
print(pd.concat([a,b],axis=1))


# In[20]:


import pandas as pd
world_champions={'Team':['India','Australia','WestIndies','Pakistan','Srilanka'],
                'ICCRank':[2,3,7,8,4],'Year':[2011,2015,1979,1922,1996],'Points':[874,787,753,673,855]}
chokers={'Team':['SouthAfrica','Newzland','Zimbabwe'], 'ICCRank':[1,5,9],'Points':[895,764,656]}
df1=pd.DataFrame(world_champions)
df2=pd.DataFrame(chokers)
print(pd.merge(df1,df2,on='Team'))


# In[21]:


import pandas as pd
a=pd.DataFrame({'key':['k0','k1','k2','k3','k4'],
               'A':['A0','A1','A2','A3','A4'],
               'B':['B0','B1','B2','B3','B4']})
b=pd.DataFrame({'key':['k0','k1','k3','k5','k6'],
               'c':['C0','C1','C2','C3','C5'],
               'D':['D0','D1','D2','D3','D5']})
print(pd.merge(a,b,on='key'))


# In[22]:


import pandas as pd
a=pd.DataFrame({'key':['k0','k1','k2','k3','k4'],
               'A':['A0','A1','A2','A3','A4'],
               'B':['B0','B1','B2','B3','B4']})
b=pd.DataFrame({'key':['k0','k1','k3','k5','k6'],
               'c':['C0','C1','C2','C3','C5'],
               'D':['D0','D1','D2','D3','D5']})
print(pd.merge(a,b,on='key',how='left'))
print(pd.merge(b,a,on='key',how='left'))
print(pd.merge(a,b,on='key',how='right'))
print(pd.merge(b,a,on='key',how='right'))
print(pd.merge(a,b,on='key',how='outer'))
print(pd.merge(b,a,on='key',how='outer'))

