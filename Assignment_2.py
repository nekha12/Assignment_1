#!/usr/bin/env python
# coding: utf-8

# ## Assignment 2

# ### Create the below pattern using nested for loop in Python.
# 

# In[19]:


r=5
for i in range(1,r+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print('')  
    
for i in range(r + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  
    
    


# ### Write a Python program to reverse a word after accepting the input from the user.

# In[22]:


word=input("Enter a word : ")
rev=word[::-1]
print("Reversed word: ",rev)


# In[ ]:




