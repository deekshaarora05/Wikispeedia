#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json
import csv


# In[2]:


file = open('short_path.json')
short_path = json.load(file)
#short_path


# In[3]:


file = open('back_clicks.json')
back_clicks = json.load(file)
#back_clicks


# In[4]:


file = open('human_path_len.json')
human_path = json.load(file)
#human_path


# In[5]:


#calculation of percentage including back clicks
same_len=0
len_1=0 #difference in length is 1
len_2=0 #difference in length is 2
len_3=0 #difference in length is 3
len_4=0 #difference in length is 4
len_5=0 #difference in length is 5
len_6=0 #difference in length is 6
len_7=0 #difference in length is 7
len_8=0 #difference in length is 8
len_9=0 #difference in length is 9
len_10=0 #difference in length is 10
len_11=0 #difference in length is more than 10
for i in range(1,51307):
    diff= human_path[str(i)]- short_path[str(i)]
    if(diff==0):
        same_len +=1
    elif(diff==1):
        len_1 +=1
    elif(diff==2):
        len_2 +=1
    elif(diff==3):
        len_3 +=1
    elif(diff==4):
        len_4 +=1
    elif(diff==5):
        len_5 +=1
    elif(diff==6):
        len_6 +=1
    elif(diff==7):
        len_7 +=1
    elif(diff==8):
        len_8 +=1
    elif(diff==9):
        len_9 +=1
    elif(diff==10):
        len_10 +=1
    else:
        len_11 +=1


# In[6]:


#percentage with back clicks
same_per= (same_len/51306)*100
len1_per= (len_1/51306)*100
len2_per= (len_2/51306)*100
len3_per= (len_3/51306)*100
len4_per= (len_4/51306)*100
len5_per= (len_5/51306)*100
len6_per= (len_6/51306)*100
len7_per= (len_7/51306)*100
len8_per= (len_8/51306)*100
len9_per= (len_9/51306)*100
len10_per= (len_10/51306)*100
len11_per= (len_11/51306)*100


# In[7]:


df1=pd.DataFrame([[same_per,len1_per,len2_per,len3_per,len4_per,len5_per,len6_per,len7_per,len8_per,len9_per,len10_per,len11_per]]
                ,columns=['Equal_Length','Larger_by_1','Larger_by_2','Larger_by_3','Larger_by_4','Larger_by_5','Larger_by_6','Larger_by_7','Larger_by_8','Larger_by_9','Larger_by_10','Larger_by_more_than_10'])
#df1


# In[8]:


df1.to_csv("percentage-paths-back.csv",index=False)


# In[9]:


#calculation of percentage without including back clicks
same_len=0
len_1=0 #difference in length is 1
len_2=0 #difference in length is 2
len_3=0 #difference in length is 3
len_4=0 #difference in length is 4
len_5=0 #difference in length is 5
len_6=0 #difference in length is 6
len_7=0 #difference in length is 7
len_8=0 #difference in length is 8
len_9=0 #difference in length is 9
len_10=0 #difference in length is 10
len_11=0 #difference in length is more than 10
for i in range(1,51307):
    h_path=human_path[str(i)]- 2*back_clicks[str(i)]
    diff= h_path-short_path[str(i)]
    if(diff==0):
        same_len +=1
    elif(diff==1):
        len_1 +=1
    elif(diff==2):
        len_2 +=1
    elif(diff==3):
        len_3 +=1
    elif(diff==4):
        len_4 +=1
    elif(diff==5):
        len_5 +=1
    elif(diff==6):
        len_6 +=1
    elif(diff==7):
        len_7 +=1
    elif(diff==8):
        len_8 +=1
    elif(diff==9):
        len_9 +=1
    elif(diff==10):
        len_10 +=1
    else:
        len_11 +=1


# In[10]:


#percentage without back clicks
same_per= (same_len/51306)*100
len1_per= (len_1/51306)*100
len2_per= (len_2/51306)*100
len3_per= (len_3/51306)*100
len4_per= (len_4/51306)*100
len5_per= (len_5/51306)*100
len6_per= (len_6/51306)*100
len7_per= (len_7/51306)*100
len8_per= (len_8/51306)*100
len9_per= (len_9/51306)*100
len10_per= (len_10/51306)*100
len11_per= (len_11/51306)*100


# In[11]:


df2=pd.DataFrame([[same_per,len1_per,len2_per,len3_per,len4_per,len5_per,len6_per,len7_per,len8_per,len9_per,len10_per,len11_per]]
                ,columns=['Equal_Length','Larger_by_1','Larger_by_2','Larger_by_3','Larger_by_4','Larger_by_5','Larger_by_6','Larger_by_7','Larger_by_8','Larger_by_9','Larger_by_10','Larger_by_more_than_10'])
#df2


# In[12]:


df2.to_csv("percentage-paths-no-back.csv",index=False)

