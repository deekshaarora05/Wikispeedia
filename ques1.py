#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv
import json
import urllib.parse


# In[2]:


reader=open("articles.tsv")
article = csv.reader(reader, delimiter="\t")
article_list=[]
i=1
for row in article:
    if(i>12):
        article_list.append(urllib.parse.unquote(row[0]))
    i+=1
article_list


# In[3]:


len(article_list)


# In[4]:


i=1
article_id=[]
article_dic={}
for article in article_list:
    article_dic[article]='A'+ str(i).zfill(4)
    article_id.append([article,'A'+str(i).zfill(4)])
    i+=1
article_id


# In[5]:


article_dic


# In[6]:


with open('article.json', 'w') as fp:
    json.dump(article_dic, fp)


# In[7]:


df=pd.DataFrame(article_id,columns=['Article_Name','Article_ID'])
df


# In[8]:


df.to_csv("article-ids.csv",index=False)


# In[ ]:




