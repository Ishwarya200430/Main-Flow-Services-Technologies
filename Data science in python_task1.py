#!/usr/bin/env python
# coding: utf-8

# In[11]:


#creating a list
my_list=[1,2,3,4]
#adding element to the list
my_list.append(6)
#removing element from the list
my_list.remove(3)
#modifying element in the list
my_list[1]=5
print(my_list)


# In[9]:


#creating dictionary
my_dict={'name':'ishu','age':'20','city':'nellore'}
#adding element to dictionary
my_dict['gender']='female'
#removing from the dictionary
del my_dict['age']
#modifying element from the dictionary
my_dict['city']='banglore'
print("updated dict:",my_dict)


# In[10]:


#cresting a set
my_set={1,2,3,4,5,6}
#adding the element in the set
my_set.add(6)
#removing the element from the set
my_set.remove(4)
#modifying element from the set
my_set.discard(2)
my_set.add(20)
print("udpated set:",my_set)


# In[ ]:



