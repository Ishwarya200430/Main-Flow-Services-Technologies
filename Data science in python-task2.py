#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd


# In[39]:


data = pd.read_csv('C:\\Users\\Ishwarya\\Downloads\\01.Data Cleaning and Preprocessing.csv')


# In[40]:


type(data)


# In[41]:


data.info


# In[42]:


data.shape


# In[43]:


data.describe()


# In[44]:


data = data.drop_duplicates()
data


# In[45]:


data.isnull()


# In[46]:


data.isnull().sum()


# In[47]:


data.notnull()


# In[48]:


data.isnull().sum().sum()


# In[49]:


data2 = data.fillna(value=0)
data2


# In[50]:


data2.isnull().sum().sum()


# In[51]:


data


# In[52]:


data2 = data.fillna(value=0)
data2


# In[53]:


data3 = data.fillna(method='pad')
data3


# In[54]:


data4=data.fillna(method='bfill')
data4


# In[55]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# In[56]:


#detect the outlines using TQR
data2.columns


# In[57]:


data2.drop(['Observation'], axis=1, inplace=True)
data2.columns


# In[58]:


Q1= data2.quantile(0.25)
Q3= data2.quantile(0.75)
IQR=Q3-Q1
print(IQR)


# In[59]:


data2=data2[~((data2<(Q1-1.5*IQR))|(data2>(Q3+1.5*IQR))).any(axis=1)]
data2


# In[60]:


data2.describe()


# In[ ]:





# In[ ]:





# In[ ]:




