#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json
import csv


# In[2]:


file1 = open(r"shortest-path-distance-matrix.txt","r+") 


# In[3]:


shortest_path=file1.readlines()


# In[4]:


shortest_path= shortest_path[17:]


# In[5]:


#shortest_path


# In[6]:


edge_dic={}
for i in range(1,4605):
    edge_dic['A'+str(i).zfill(4)]=list()
#edge_dic


# In[7]:


edge_list=[]
i=1
for ele in shortest_path:
    j=1
    x='A'+str(i).zfill(4)
    for dist in ele:
        if(dist=='1'):
            y='A'+str(j).zfill(4)
            edge_list.append([x,y])
            edge_dic[x].append(y)
        j+=1
    i+=1
#edge_dic


# In[8]:


#edge_list


# In[9]:


df=pd.DataFrame(edge_list, columns=['From_ArticleID','To_ArticleID'])


# In[11]:


with open("edge_dic.json", "w") as fp: 
    json.dump("edge_dic", fp) 


# In[12]:


df.to_csv('edges.csv', index=False)


# In[ ]:




