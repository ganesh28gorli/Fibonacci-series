#!/usr/bin/env python
# coding: utf-8

# # fibonacci series 

# In[15]:


# n is the number of terms to be printed in fibonacci series


# In[16]:


n = int(input("enter number of terms: "))


# In[17]:


# assigning first two terms of the sequence


# In[18]:


a=0
b=1


# In[19]:


#checking if the number of terms of sequence(n), given by the user is valid or not.if number is valid the fibinacci sequence.


# In[20]:


if n<=0:
    print("enter number greater than zero") 
    print(a)
elif n == 1:
    print(a)   
else:
    print(a)
    print(b)
    
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)           


# In[ ]:





# In[ ]:




