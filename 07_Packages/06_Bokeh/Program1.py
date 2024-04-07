#!/usr/bin/env python
# coding: utf-8

# In[8]:


from bokeh.plotting import output_file,show,figure
import pandas as pd
dataset=pd.DataFrame(columns=["X","Y"])
dataset["X"]=[1,2,3,4,5]
dataset["Y"]=[1,4,9,16,25]
output_file=("Scatter_Charter.html")
p=figure(plot_width=500,plot_height=400)
p.circle(dataset["X"],dataset["Y"],size=10)
show(p)


# In[ ]:




