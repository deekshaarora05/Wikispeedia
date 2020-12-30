#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import json
import pandas as pd
import urllib.parse
import itertools
import networkx as nx


# In[2]:


csv_file = open("edges.csv")
edges = csv.reader(csv_file)
edge_list=[]
i=1
for row in edges:
    if(i>1):
        edge_list.append(row)
    i+=1
#edge_list


# In[3]:


articles=[]
with open('article-ids.csv', 'r') as read:
    csv_reader = csv.reader(read)
    for row in csv_reader:
          articles.append(row[1])
articles=articles[1:]


# In[4]:


g=nx.Graph()
for edge in edge_list:
    g.add_edge(edge[0],edge[1])
#g.number_of_edges()


# In[5]:


component = nx.connected_components(g)
component_list=[]
for index,component in enumerate(component):
    component_list.append(component)
#component_list


# In[6]:


isolated_vertices = set(articles)-component_list[0]-component_list[1]
#isolated_vertices


# In[7]:


node_edge_dia=[]
for val in component_list:
    subgraph = g.subgraph(val).copy()
    x=subgraph.number_of_nodes()
    e=subgraph.number_of_edges()
    d=nx.diameter(subgraph)
    node_edge_dia.append([x,e,d])
#node_edge_dia


# In[8]:


df=pd.DataFrame(node_edge_dia,columns=['Nodes','Edges','Diameter'])
for vertex in isolated_vertices:
    df.loc[len(df.index)] = [1, 0, 0] 


# In[9]:


#df


# In[10]:


df.to_csv('graph-components.csv',index=False)

