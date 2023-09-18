#!/usr/bin/env python
# coding: utf-8

# In[174]:


import pandas as pd
import numpy as np


# ## Question 1

# In[175]:


pd.__version__


# In[176]:


df = pd.read_csv("E:/Downloads/raw.githubusercontent.com_alexeygrigorev_datasets_master_housing.csv")


# ## Question 2

# In[177]:


df


# In[178]:


df.shape


# ## Question 3

# In[179]:


df.isnull().sum()


# ## Question 4

# In[180]:


df['ocean_proximity'].nunique()


# ## Question 5

# In[181]:


df[df['ocean_proximity'] == 'NEAR BAY']['median_house_value'].mean().round(3)


# ## Question 6

# In[182]:


df['total_bedrooms'].mean().round(3)


# In[183]:


df['total_bedrooms'].fillna(value=537.871, inplace=True)


# In[184]:


df.isnull().sum()


# In[185]:


df['total_bedrooms'].mean().round(3)


# ## Question 7

# In[186]:


df = df[df['ocean_proximity'] == 'ISLAND']


# In[187]:


df = df[['housing_median_age', 'total_rooms', 'total_bedrooms']]
df


# In[188]:


X = np.array(df)
X


# In[189]:


XTX = np.matmul(X.T, X)
XTX


# In[190]:


XTX_inv = np.linalg.inv(XTX)
XTX_inv


# In[191]:


y = np.array([950, 1300, 800, 1000, 1300])
y


# In[192]:


Z = np.matmul(XTX_inv, X.T)
Z


# In[193]:


w = np.matmul(Z, y)
w

