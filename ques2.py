#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import urllib.parse
import json
import csv


# In[2]:


reader=open("categories.tsv")
category = csv.reader(reader, delimiter="\t")
category_set=set()
i=1
for row in category:
    if(i>13):
        category_set.add(urllib.parse.unquote(row[1]))
    i+=1
#category_set


# In[3]:


categories=list(category_set)
#categories


# In[5]:


categories.sort()


# In[7]:


category_set=set()
for element in categories:
    l=element.split('.')
    #print(l)
    x=len(l)
    for i in range(0,x):
        tmp=l[0]
        for j in range(1,i+1):
            tmp+='.'+l[j]
        category_set.add(tmp)
#category_set


# In[9]:


cat_list=list(category_set)


# In[10]:


#cat_list


# In[11]:


cat_list.sort()
#cat_list


# In[12]:


freq={1:[],2:[],3:[],4:[]}
#freq


# In[13]:


for ele in cat_list:
    x=ele.split('.')
    y=len(x)
    freq[y].append(ele)
#freq


# In[14]:


x=1
category_list=[]
category_dic={}
for key in range(1,5):
    for val in freq[key]:
        category_dic[val]='C'+str(x).zfill(4)
        x+=1


# In[16]:


category_list=[]
for ele in cat_list:
    category_list.append([ele,category_dic[ele]])
#category_list


# In[17]:


with open('category.json', 'w') as fp:
    json.dump(category_dic, fp)


# In[18]:


df=pd.DataFrame(category_list, columns=['Category_Name','Category_ID'])


# In[19]:


df.to_csv("category-ids.csv",index=False)


# In[ ]:




