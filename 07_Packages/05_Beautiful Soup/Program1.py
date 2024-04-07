#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from bs4 import BeautifulSoup
r=requests.get("https://www.python.org/")
c=r.content
#print(c)
soup=BeautifulSoup(c,"html.parser")
print(soup.prettify())


# In[9]:


import requests
from bs4 import BeautifulSoup
r=requests.get("https://www.python.org/")
c=r.content
soup=BeautifulSoup(c,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))


# In[ ]:




