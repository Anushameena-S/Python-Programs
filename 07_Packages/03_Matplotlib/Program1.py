#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()


# In[8]:


import matplotlib.pyplot as plt
y_values=[1,2,3,4,10]
x_values=[]
for i in y_values:
    x_values.append(i**2)
print(x_values)
plt.plot(x_values,y_values)
plt.show()


# In[19]:


import numpy as np
import matplotlib.pyplot as plt
y=np.arange(0,5,0.1)
print(y)
print([i**2 for i in y])
plt.plot([i**2 for i in y])
plt.show()


# In[27]:


import matplotlib.pyplot as plt
x=range(5)
plt.plot(x, [x1 for x1 in x],label='linear')
plt.plot(x,[x1*x1 for x1 in x],label='squared')
plt.plot(x,[x1*x1*x1 for x1 in x],label='cubed')
plt.grid(True)
#plt.axis([-1,5,-1,10])
plt.xlim(-1,5)
plt.ylim(-1,100)
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.title('Learning....')
plt.legend()
plt.savefig('myplot.png')
plt.show()


# In[4]:


import matplotlib.pyplot as plt
import numpy as np
y=np.random.randn(5,10)
print(y)
plt.hist(y)
plt.show()


# In[5]:


import matplotlib.pyplot as plt
plt.bar([1.2,2.6,4.8],[44,56,89])
plt.show()


# In[8]:


import matplotlib.pyplot as plt
dict1={'a':56,'b':98,'c':67,'d':70}
for i,key in enumerate(dict1):
    plt.bar(i,dict1[key])


# In[13]:


import matplotlib.pyplot as plt
import numpy as np
dict1={'a':56,'b':98,'c':67,'d':70}
for i,key in enumerate(dict1):
    plt.bar(i,dict1[key])
#plt.xticks(np.arange(len(dict1)),dict1.keys())
plt.xticks([0,1,2,3],['A-Tick','B-Tick','C-Tick','D-Tick'])
plt.show()


# In[14]:


import matplotlib.pyplot as plt
plt.figure(figsize=(3,3))
x=[40,21,34]
labels=['Bikes','Cars','Buses']
plt.pie(x,labels=labels)
plt.show()


# In[17]:


import matplotlib.pyplot as plt
import numpy as np
x=np.random.rand(100)
print(x)
y=np.random.rand(100)
print(y)
plt.scatter(x,y)
plt.show()


# In[18]:


import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
print(y)
plt.plot(y,'y')
plt.plot(y+5,'m')
plt.plot(y+10,'c')
plt.show()


# In[19]:


import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,100)
plt.plot(y,'--',y*5,'-.',y*10,':')
plt.show()


# In[20]:


import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3,0.2)
print(y)
plt.plot(y,'*',y+0.5,'o',y+1,'D',y+2,'^',y+3,'s')
plt.show()

