#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json
import csv
import urllib.parse
import networkx as nx


# In[2]:


reader=open("categories.tsv")
category = csv.reader(reader, delimiter="\t")
category_list=[]
i=1
for row in category:
    if i>13:
        category_list.append([urllib.parse.unquote(row[0]),urllib.parse.unquote(row[1])])
    i+=1
#category_list


# In[3]:


file = open('category.json')
categoryId = json.load(file)
#categoryId


# In[4]:


with open("article.json", "r") as f:
    article_ids = json.load(f)


# In[5]:


artCategory={}
for key in article_ids.keys():
    artCategory[key]=set()


# In[6]:


for ele in category_list:
    l=ele[1].split('.')
    x=len(l)
    tmp="subject"
    #print(ele[1])
    artCategory[ele[0]].add(categoryId[tmp])
    for i in range(1,x):
        tmp+='.'+l[i]
        #print(tmp)
        artCategory[ele[0]].add(categoryId[tmp])
#artCategory


# In[7]:


articleAllCat={}
for (key,val) in artCategory.items():
    articleAllCat[key]=list(val)
#articleAllCat


# In[8]:


for (key,val) in articleAllCat.items():
    if(val==[]):
        articleAllCat[key].append('C0001')


# In[9]:


with open('articleAllCategory.json', 'w') as fp:
    json.dump(articleAllCat, fp)


# In[10]:


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


# In[11]:


category_id=[]
for i in range(1,147):
    category_id.append('C'+str(i).zfill(4))
#category_id


# In[12]:


paths_traversed={}
category_traversed={}
short_paths_traversed={}
short_category_traversed={}
for ele in category_id:
    paths_traversed[ele]=0
    category_traversed[ele]=0
    short_paths_traversed[ele]=0
    short_category_traversed[ele]=0


# In[13]:


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
            for artcat in articleAllCat[node]:
                category_traversed[artcat]+=1
                category_set.add(artcat)
    for ele in category_set:
        paths_traversed[ele]+=1


# In[16]:


with open('edges.csv', newline='') as f:
    reader = csv.reader(f)
    edge_list = list(reader)
edge_list=edge_list[1:]


# In[17]:


G = nx.DiGraph()
G.add_edges_from(edge_list)
G


# In[18]:


artIdCat={}
for (key,val) in artCategory.items():
    artIdCat[article_ids[key]]=val
#artIdCat


# In[19]:


for (k,v) in artIdCat.items():
    if 'C0001' not in v:
        artIdCat[k].add('C0001')


# In[20]:


for pair in source_des_pairs:
    route = nx.shortest_path(G, article_ids[pair[0]], article_ids[pair[1]])
    short_category_set=set()
    for node in route:
        for artcat in artIdCat[node]:
            short_category_traversed[artcat]+=1
            short_category_set.add(artcat)
    for ele in short_category_set:
        short_paths_traversed[ele]+=1


# In[21]:


category_path_list=[]
for ele in category_id:
    category_path_list.append([ele,paths_traversed[ele],category_traversed[ele],short_paths_traversed[ele],short_category_traversed[ele]])
#category_path_list


# In[22]:


df=pd.DataFrame(category_path_list, columns=['Category_ID','Number_of_human_paths_traversed','Number_of_human_times_traversed','Number_of_shortest_paths_traversed','Number_of_shortest_times_traversed'])
#df


# In[23]:


df.to_csv("category-subtree-paths.csv",index=False)

