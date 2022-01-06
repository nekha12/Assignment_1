#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# ### Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[6]:


for x in range(2000,3200):
    if (x% 7 ==0) and (x%5!=0):
        print(x,end=',')


# ### Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[15]:


first_name=input("Enter first name :")
last_name=input("Enter last name :")
print(first_name[::-1],last_name[::-1])


# ### Write a Python program to find the volume of a sphere with diameter 12 cm.Formula: V=4/3 * π * r 3

# In[19]:


import math
d= 12
r=d/2
volume=4/3*math.pi*pow(r,3)
print("volume of sphere",volume)


# In[ ]:





# In[ ]:





# In[ ]:




