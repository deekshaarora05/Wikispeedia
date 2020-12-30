#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import json
import csv
import urllib.parse
import networkx as nx


# In[3]:


file=open("article_leafCategory.json")
articleCategory=json.load(file)
#articleCategory


# In[4]:


file=open("category.json")
category_ids=json.load(file)
#category_ids


# In[5]:


i=1
reader=open("paths_finished.tsv")
paths = csv.reader(reader, delimiter="\t")
paths_finished=[]
for row in paths:
    if(i>16):
        l= row[3].split(';')
        x=[]
        for ele in l:
            x.append(urllib.parse.unquote(ele))
        paths_finished.append(x)
    i+=1
#paths_finished


# In[6]:


category_id=[]
for i in range(1,147):
    category_id.append('C'+str(i).zfill(4))
#category_id


# In[7]:


paths_traversed={}
category_traversed={}
short_paths_traversed={}
short_category_traversed={}
for ele in category_id:
    paths_traversed[ele]=0
    category_traversed[ele]=0
    short_paths_traversed[ele]=0
    short_category_traversed[ele]=0


# In[8]:


source_des_pairs=[]
for path in paths_finished:
    source_des_pairs.append([path[0],path[-1]])
    rev_path=reversed(path)
    category_set=set()
    back_click=0
    for node in rev_path:
        if(back_click!=0):
            if(node=='<'):
                back_click+=1
            else:
                back_click-=1
        elif(node=='<'):
            back_click+=1
        else:
            for artcat in articleCategory[node]:
                category_traversed[artcat]+=1
                category_set.add(artcat)
    for ele in category_set:
        paths_traversed[ele]+=1


# In[11]:


with open('edges.csv', newline='') as f:
    reader = csv.reader(f)
    edge_list = list(reader)
edge_list=edge_list[1:]
#edge_list


# In[12]:


G = nx.DiGraph()
G.add_edges_from(edge_list)


# In[15]:


with open("article.json", "r") as f:
    article_ids = json.load(f)
#article_ids


# In[16]:


artIdCat={}
for (key,val) in articleCategory.items():
    artIdCat[article_ids[key]]=val
#artIdCat


# In[17]:


for pair in source_des_pairs:
    route = nx.shortest_path(G, article_ids[pair[0]], article_ids[pair[1]])
    short_category_set=set()
    for node in route:
        for artcat in artIdCat[node]:
            short_category_traversed[artcat]+=1
            short_category_set.add(artcat)
    for ele in short_category_set:
        short_paths_traversed[ele]+=1


# In[20]:


category_path_list=[]
for ele in category_id:
    category_path_list.append([ele,paths_traversed[ele],category_traversed[ele],short_paths_traversed[ele],short_category_traversed[ele]])
#category_path_list


# In[21]:


df=pd.DataFrame(category_path_list, columns=['Category_ID','Number_of_human_paths_traversed','Number_of_human_times_traversed','Number_of_shortest_paths_traversed','Number_of_shortest_times_traversed'])
#df


# In[22]:


df.to_csv("category-paths.csv",index=False)

