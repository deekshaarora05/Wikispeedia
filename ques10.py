#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import csv
import json
import urllib.parse
import networkx as nx


# In[3]:


i=1
reader=open("paths_unfinished.tsv")
paths = csv.reader(reader, delimiter="\t")
paths_unfinished=[]
for row in paths:
    if(i>17):
        s=urllib.parse.unquote(row[3].split(';')[0])
        d=urllib.parse.unquote(row[4] )   
        paths_unfinished.append([s,d])
    i+=1


# In[4]:


with open("article.json", "r") as f:
    article_ids = json.load(f)
#article_ids


# In[5]:


with open("articleAllCategory.json", "r") as f:
    artAllCat = json.load(f)
#artAllCat


# In[26]:


for ele in paths_unfinished:
    for node in ele:
        if(article_ids.get(node)==None):
            artAllCat[node]=['C0001']


# In[41]:


unfinish_cat_pair={}
x=1
for ele in paths_unfinished:
    s_cat=artAllCat[ele[0]]
    d_cat=artAllCat[ele[1]]
    all_permutation=[[i,j] for i in s_cat for j in d_cat]
    for per in all_permutation:
        unfinish_cat_pair[tuple(per)]=unfinish_cat_pair.get(tuple(per),0)+1
#unfinish_cat_pair


# In[29]:


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


# In[30]:


finish_cat_pair={}
x=1
for ele in paths_finished:
    s_cat=artAllCat[ele[0]]
    d_cat=artAllCat[ele[1]]
    all_permutation=[[i,j] for i in s_cat for j in d_cat]
    for per in all_permutation:
        finish_cat_pair[tuple(per)]=finish_cat_pair.get(tuple(per),0)+1
#finish_cat_pair


# In[31]:


catPair_set=set()
for key in unfinish_cat_pair.keys():
    catPair_set.add(key)
for key in finish_cat_pair.keys():
    catPair_set.add(key)
#catPair_set


# In[35]:


category_pair=[]
for ele in catPair_set:
    unfinish=unfinish_cat_pair.get(ele,0)
    finish=finish_cat_pair.get(ele,0)
    total=unfinish + finish
    unfinish_per= (unfinish/total)*100
    finish_per= (finish/total)*100
    category_pair.append([ele[0],ele[1],finish_per,unfinish_per])
#category_pair


# In[36]:


df=pd.DataFrame(category_pair,columns=['From_Category','To_Category','Percentage_of_finished_paths','Percentage_of_unfinished_paths'])


# In[37]:


df.sort_values(['From_Category', 'To_Category'], ascending=[True, True],inplace=True)


# In[38]:


df.to_csv("category-pairs.csv",index=False)


# In[ ]:




