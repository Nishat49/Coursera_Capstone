#!/usr/bin/env python
# coding: utf-8

# ## Segmentation and Clustering Neighbourhood in Toronto
# 

# In[6]:


import pandas as pd
import requests


# In[7]:


url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=header)

df = pd.read_html(r.text)
df_raw = df[0]


# # data set for canada

# In[8]:


df_raw.head()


# In[9]:


df_raw.shape


# In[11]:


df_canada_data = df_raw[:]


# # Borough Not Assigned for 77 rows so we will filter it

# In[12]:


(df_canada_data['Borough'] == 'Not assigned').value_counts()


# In[13]:


df_canada_data = df_canada_data[df_canada_data['Borough'] != 'Not assigned']


# In[14]:


df_canada_data.shape


# # Postal Code repeated - 0

# In[15]:


if False in (df_canada_data['Postal Code'].value_counts() > 1).tolist():
    print("Zero")


# # Rows with Neighborhood not assigned - 0

# In[16]:


(df_canada_data['Neighborhood'] == 'Not assigned').value_counts()


# # Shape of Borough is

# In[17]:


df_canada_data.shape


# # Canada Boroughs and Neighborhoods

# In[32]:


df_coordinates = pd.read_csv('E:\COURSERA\IBM Professional Data Science\capstone project\Geospatial_Coordinates.csv')


# In[33]:


df_coordinates.head()


# In[35]:


df_canada=pd.read_csv('E:\COURSERA\IBM Professional Data Science\capstone project\canada_data.csv')


# In[ ]:




