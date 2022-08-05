#!/usr/bin/env python
# coding: utf-8

# In[44]:


import numpy as np
import pandas as pd

dictionary = { 
    "name" : ["Anastasia","Dima","Katherine","James","Emily","michael","matthew","laura","kevin","jonas"] ,
    "score" : [12.5 , 9 , 16.5 , np.nan , 9 , 20 , 14.5 , np.nan , 8 , 9 ,] ,
    "attempts" : [1,3,2,3,2,3,1,1,2,1 ,] ,
    "qualify" : ["yes","no","yes","no","no","yes","yes","no","no","yes" ,] ,
    "labels" : ["a","b","c","d","e","f","g","h","i","j" ,] 
} 


# In[45]:


df = pd.DataFrame.from_dict(dictionary)
df     # displaying the data frame of the dictionary :


# In[46]:


df.head(3)   #displaying the first 3 lines


# In[47]:


df=df.dropna()
df


# In[48]:


df[["name","score"]] # extracting the "name" and "score" values


# In[49]:


K = { "name" : ["suresh"] , "score" : [15.5 ], "attempts" : [1 ], "qualify" : ["yes"] ,}
df1 = pd.DataFrame.from_dict(K)
df1    #adding a new student


# In[50]:


df = pd.concat([df , df1])
df.drop("attempts" ,axis = 1) # deleting "attempts"


# In[51]:


df["Success"] = np.where(df["score"] >= 10 , 1 , 0 )
df


# In[52]:


df.to_csv('my_data.csv')


# In[ ]:




