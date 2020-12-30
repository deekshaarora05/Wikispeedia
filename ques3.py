#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json
import csv
import urllib.parse


# In[2]:


reader=open("categories.tsv")
category = csv.reader(reader, delimiter="\t")
category_list=[]
i=1
for row in category:
    if i>13:
        category_list.append([urllib.parse.unquote(row[0]),urllib.parse.unquote(row[1])])
    i+=1


# In[3]:


file = open('category.json') # Contains the neighbors of each district
categoryId = json.load(file)
#categoryId


# In[4]:


file = open('article.json') # Contains the neighbors of each district
articleId = json.load(file)
#articleId


# In[5]:


artCategory={}
for key in articleId.keys():
    artCategory[key]=[]
#artCategory


# In[6]:


for ele in category_list:
    artCategory[ele[0]].append(categoryId[ele[1]])
#artCategory


# In[7]:


for key,val in artCategory.items():
    if(val==[]):
        artCategory[key].append('C0001')


# In[8]:


article_leafCategory=[]
for key in articleId.keys():
    x=sorted(artCategory[key])
    y=','.join(x)
    article_leafCategory.append([articleId[key],y])
#article_leafCategory


# In[9]:


df=pd.DataFrame(article_leafCategory, columns=['Article_ID','Category_ID'])


# In[13]:


df.to_csv('article-categories.csv',index=False)


# In[14]:


with open('article_leafCategory.json', 'w') as fp:
    json.dump(artCategory, fp)


# In[ ]:




