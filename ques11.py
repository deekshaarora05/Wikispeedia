#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv
import json
import urllib.parse
from statistics import mean
import networkx as nx


# In[2]:


i=1
reader=open("paths_finished.tsv")
paths = csv.reader(reader, delimiter="\t")
paths_finished=[]
for row in paths:
    if(i>16):
        l=row[3].split(';')
        s=urllib.parse.unquote(l[0])
        d=urllib.parse.unquote(l[-1])
        paths_finished.append([s,d])
    i+=1
#paths_finished


# In[3]:


with open("articleAllCategory.json", "r") as f:
    artAllCat = json.load(f)
#artAllCat


# In[4]:


with open("human_path_len.json", "r") as f:
    total_len = json.load(f)
#total_len


# In[5]:


with open("short_path.json", "r") as f:
    short_path = json.load(f)
#short_path


# In[6]:


with open("back_clicks.json", "r") as f:
    back_clicks = json.load(f)
#back_clicks


# In[7]:


finish_cat_pair={}
x=1
for ele in paths_finished:
    s_cat=artAllCat[ele[0]]
    d_cat=artAllCat[ele[1]]
    human_path=total_len[str(x)]-2*back_clicks[str(x)]
    ratio=human_path/short_path[str(x)]
    x+=1
    all_permutation=[[i,j] for i in s_cat for j in d_cat]
    for per in all_permutation:
        finish_cat_pair[tuple(per)]=finish_cat_pair.get(tuple(per),[])
        finish_cat_pair[tuple(per)].append(ratio)
#finish_cat_pair


# In[8]:


finish_list=[]
for (key,val) in finish_cat_pair.items():
    avg=mean(val)
    finish_list.append([key[0],key[1],avg])
#finish_list


# In[9]:


finish_list.sort()


# In[10]:


df=pd.DataFrame(finish_list,columns=['From_Category','To_Category','Ratio_of_human_to_shortest'])


# In[11]:


df.to_csv("category-ratios.csv",index=False)


# In[ ]:




