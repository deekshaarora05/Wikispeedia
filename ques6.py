#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json
import csv
import urllib.parse


# In[2]:


i=1
reader=open("paths_finished.tsv")
paths_finished = csv.reader(reader, delimiter="\t")
paths=[]
for row in paths_finished:
    if(i>16):
        l= row[3].split(';')
        x=[]
        for ele in l:
            x.append(urllib.parse.unquote(ele))
        paths.append(x)
    i+=1


# In[4]:


file = open('article.json') 
article_ids = json.load(file)
#article_ids


# In[5]:


file1 = open(r"shortest-path-distance-matrix.txt","r+") 
shortest_path=file1.readlines()
shortest_path= shortest_path[17:]


# In[6]:


with_back_clicks=[]
back_clicks={}
total_path={}
short_path={}
path_id=1
for path in paths:
    source=article_ids[path[0]]
    dest=article_ids[path[-1]]
    s=int(source[1:])
    d=int(dest[1:])
    s_path=shortest_path[s-1][d-1]
    b_click=0
    human_path=0
    for ele in path:
        human_path+=1
        if(ele=='<'):
            b_click+=1
    x=int(s_path)
    human_path-=1
    ratio=human_path/x
    with_back_clicks.append([human_path,x,ratio])
    back_clicks[path_id]=b_click
    short_path[path_id]=int(s_path)
    total_path[path_id]=human_path
    path_id+=1
#with_back_clicks    


# In[8]:


without_back_clicks=[]
for i in range(1,51307):
    human_path=total_path[i] - 2*back_clicks[i]
    s_path=short_path[i]
    ratio=human_path/s_path
    without_back_clicks.append([human_path,s_path,ratio])
#without_back_clicks


# In[9]:


df1=pd.DataFrame(with_back_clicks,columns=['Human_Path_Length','Shortest_Path_Length','Ratio'])
#df1


# In[10]:


df1.to_csv("finished-paths-back.csv",index=False)


# In[11]:


df2=pd.DataFrame(without_back_clicks,columns=['Human_Path_Length','Shortest_Path_Length','Ratio'])
#df2


# In[12]:


df2.to_csv("finished-paths-no-back.csv",index=False)


# In[13]:


with open("human_path_len.json", "w") as fp: 
    json.dump(total_path, fp) 


# In[14]:


with open("back_clicks.json", "w") as fp: 
    json.dump(back_clicks, fp) 


# In[15]:


with open("short_path.json", "w") as fp: 
    json.dump(short_path, fp) 

