#!/usr/bin/env python
# coding: utf-8

# In[1]:


10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~


# In[51]:


def derive(self, excs):
   return Errors(excs, self.exit_code)divide_numbers = 7 / 0
print(divide_numbers) = sys.exception().__traceback
 raise OtherException(...).with_traceback(tb)


# In[82]:


lst = [1, 2, 3]
print(lst[5])  # Raises IndexError


# In[84]:


my_dict = {"a": 1}
print(my_dict["b"])  # Raises KeyErroropen("nonexistent_file.txt")  # Raises FileNotFoundError


# In[86]:


open("nonexistent_file.txt")  # Raises FileNotFoundError


# In[88]:


"hello".non_existent_method()  # Raises AttributeError


# In[90]:


import math
math.exp(1000)  # May raise OverflowError1 / 0  # Raises ZeroDivisionError


# In[92]:


1 / 0  # Raises ZeroDivisionError


# In[96]:


"2" + 2  # Raises TypeError


# In[98]:


int("abc")  # Raises ValueError

