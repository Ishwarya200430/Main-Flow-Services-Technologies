#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('C:\\Users\\Ishwarya\\Downloads\\disney_plus_titles.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.isna().sum()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


type(df)


# In[9]:


df=df.drop_duplicates()
df


# In[10]:


df.columns


# In[11]:


df.hist(bins=50,grid=False,figsize=(20,15));


# In[39]:


questions = ["1.how many chaneels are rated and its value  ?",
            "2.how many are listed_in the disney list of channels also represent?",
            "3.how many countries list them and their appropriate vlaues",
            "4.specify the realising years grapically increasing or decreasing  ",
            "5.check the duration approximately ",
            "6.is Movie or Tv show is high ? which type is high? ",
            "7.specify dates added approximately by graphically",
            "8.check the ids in desney plus ,Is gradually?"]
questions


# In[13]:


df.rating.value_counts()


# In[34]:


#Answer-01 in bar chart
df.rating.value_counts().plot(kind='bar',color=["blue","red"])
plt.title("Rated to Disney ")
plt.xlabel("Rated channels")
plt.ylabel("value range")


# In[38]:


#Answer-01 in pie chart
df.rating.value_counts().plot(kind='pie',figsize=(10,6))
plt.legend(["Rated -10","Rated -9","Rated -8","Rated -7","Rated -6","Rated -5","Rated -4","Rated -3","Rated -2"]);


# In[24]:


#Answe-02
df.listed_in.value_counts().plot(kind='bar',color=["blue","red","pink","orange"])
plt.title("Listed to Disney ")
plt.xlabel("Listed channels")
plt.ylabel("Amount")


# In[23]:


#Answer-03
df.country.value_counts().plot(kind='bar',color=["blue","red"])
plt.title("No of countries listed ")
plt.xlabel("List of countries")
plt.ylabel("value")


# In[25]:


#Answer-04
sns.displot(x='release_year',data=df,bins=10,kde=True);


# In[26]:


#Answer-04
sns.displot(x='release_year',data=df,bins=10,kde=False);


# In[27]:


#Answer-05
sns.displot(x='duration',data=df,bins=30,kde=True,color='brown')


# In[29]:


#Answer-06
df.type.value_counts().plot(kind='pie',figsize=(10,6))
plt.legend(["Movie","TV show"]);


# In[30]:


#Answer-07
sns.displot(x='date_added',data=df,bins=10,kde=True);


# In[33]:


#Answer-08
sns.displot(x='show_id',data=df,bins=10,kde=True);


# In[ ]:




