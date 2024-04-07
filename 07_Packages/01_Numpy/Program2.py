#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
b=np.array([[2,3,5,9],[5,6,7,8],[8,9,7,5]])
print("The numpy array is :", b)
print("The numpy array data type is :", type(b))


# In[5]:


import numpy as np
c=np.zeros([5,3])
d=np.zeros([10,10])
print("The zero array is :", c)
print("The zero array of 10 dim is :", d)


# In[6]:


import numpy as np
e=np.arange(0,50)
print("The single dim array got from range fun is :\n", e)


# In[8]:


import numpy as np
vector=np.linspace(0,20,5)
print("The vector values are :", vector)
vector1=np.linspace(1,30,4)
print("The vector1 values are :", vector1)
vector2=np.linspace(0,40,11)
print("The vector2 values are :", vector2)


# In[9]:


import numpy as np
list1=[8,6,4,3]
arr=np.asarray(list1)
print("The list converted to array :", arr)


# 

# In[32]:


import numpy as np
arr=np.zeros(10)
print("The zero array is :", arr)
print("The shape of array is :", arr.shape)
arr1=arr.reshape(2,5)
print("The reshaped array is :", arr1)
arr2=arr.reshape(5,2)
print("The reshaped array is :",arr2)
arr3=arr.reshape(5,1,2)
print("The reshaped array is :", arr3)
arr4=arr3.ravel()
print("The flattened array is :", arr4)


# In[38]:


import numpy as np
arr=np.arange(2,20)
element=arr[10]
element1 =arr[:10]
element2=arr[10:]
print("The array values are :", arr)
print("The 10th element is :", element)
print("The type of element is :", type(element))
print("Before 10th element :", element1)
print("The type of element1 is :", type(element1))
print("After 10th element :", element2)
print("The type of element2 is :", type(element2))


# In[42]:


import numpy as np
arr=np.arange(20)
print("The array values are :", arr)
arr_slice=slice(0,10,2)
print("The array slice values are :", arr_slice)
print(arr[arr_slice])


# In[59]:


import numpy as np
a=np.array([[2,3,5],[6,4,5],[3,2,1]])
b=np.array([3,4,5,6,7,8,9])
print([a[0:3,1:3]])
print("The shape of a array is :", a.shape)
print("The shape of b array is :", b.shape)
print("The dim of a array is :", a.ndim)
print("The dim of b array is :", b.ndim)
print("The item size of a is :", a.itemsize)
print("The item size of b is :", b.itemsize)


# In[62]:


x=np.empty([8,5],dtype=int)
print("The initialized array is :", x)


# In[70]:


import numpy as np
arr=np.arange(50)
np.savetxt('newfile.txt',arr)
arr1=([[3,4,5],[5,4,1],[7,5,4]])
np.savetxt('newfile1.txt',arr1)
arr3=np.loadtxt('newfile.txt')
print("The newfile contents are :\n", arr3)
arr4 = np.loadtxt('newfile1.txt')
print("The newfile1 contents are :\n", arr4)






