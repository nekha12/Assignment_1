#!/usr/bin/env python
# coding: utf-8

# ## Assignment 4

# #### 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
# #### area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# #### Function to take the length of the sides of triangle from user should be defined in the parent
# #### class and function to calculate the area should be defined in subclass.

# In[18]:


class triangle:
    def __init__(self,a,b,c):
        self.a=float(a)
        self.b=float(b)
        self.c=float(c)
a=input("a=")
b=input("b=")
c=input("c=")

class area_triangle(triangle):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
    def get_area(self):
        s= (self.a+self.b+self.c)*0.5
        area=(s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return area
t=area_triangle(a,b,c)

print("area : ",t.get_area())


# ### Write a function filter_long_words() that takes a list of words and an integer n and returns
# ### the list of words that are longer than n.

# In[28]:


def filter_long_words(list_words,n):
    inputlist=[]
    for word in list_words:
        if len(word)>n:
            inputlist.append(word)
    return inputlist
word_list=['kite','red','tree']
n=3
filter_long_words(word_list,n)


# ### 2.1 Write a Python program using function concept that maps list of words into a list of integers
# ### representing the lengths of the corresponding words.

# In[31]:


def list_words(w):
    output_list=[]
    for i in w:
        l=len(i)
        output_list.append(l)
    return output_list
words_list=['kite','kingkong','karate']
integer_list=list_words(words_list)
print(integer_list)


# ### 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# ### it is a vowel, False otherwise.

# In[56]:


def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char not in vowels:
        return False
    return True
k=input("Enter the character: ")
is_vowel(k)


# In[ ]:




