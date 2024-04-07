#!/usr/bin/env python
# coding: utf-8

# In[3]:


import folium
m=folium.Map(location=[12.958016,77.744033])

#fg=folium.FeatureGroup(name="Volcanoes")


# In[5]:


m.save("folium.html")


# In[11]:


folium.Map(location=[12.958016,77.744033],zoom_start=21)


# In[14]:


folium.Map(location=[12.958016,77.744033],zoom_start=12,tiles='cartodbpositron'


# In[15]:


folium.Map(location=[12.958016,77.744033],zoom_start=12,tiles='Stamen Terrain')


# In[16]:


import folium
map=folium.Map(location=[12.958016,77.744033],zoom_start=12,tiles='cartodbpositron')
fg=folium.FeatureGroup(name="Important Locations")
fg.add_child(folium.Marker(
    location=[12.9596,77.744033],
    popup="Loc 1",
    icon=folium.Icon(color="green")))
map.add_child(fg)
map.save('folium1.html')


# In[47]:


import folium
map=folium.Map(location=[12.958016,77.744033],zoom_start=5,tiles='cartodbpositron')
fg=folium.FeatureGroup(name="Important Locations")
for coordinate in ([10.9596,79.44033],[10.1596,77.144033]):
    fg.add_child(folium.Marker(
        location=[coordinate[0],coordinate[1]],
        popup="Favourites",
        icon=folium.Icon(color="blue")))
map.add_child(fg)
map.save('folium2.html')


# In[ ]:




