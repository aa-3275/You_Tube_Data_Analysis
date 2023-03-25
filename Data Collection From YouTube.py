#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 


# In[2]:


path=r'F:\Python_Data_Analyis_Project\additional_data-20230323T140537Z-001\additional_data'


# In[3]:


Files=os.listdir(path)


# In[4]:


Files_csv= [Files[i] for i in range (0, len(Files),2)]


# In[5]:


Files_csv[0].split('.')[0][0:2]


# In[6]:


Full_df=pd.DataFrame()
for file in Files_csv:
    current_df= pd.read_csv(path +'/'+ file, encoding= 'iso-8859-1', error_bad_lines=False)
    current_df['Country']= file.split('.')[0][0:2]
    Full_df= pd.concat([Full_df,current_df])


# In[7]:


Full_df.head()


# In[8]:


Full_df.shape


# ## Which Cateogry has maximum Likes?

# In[9]:


Full_df['category_id'].unique()


# In[10]:


Cat= pd.read_csv(r'F:\Python_Data_Analyis_Project\category_file.txt',sep=': \t\t')


# In[11]:


Cat


# In[12]:


Cat.reset_index(inplace=True)


# In[13]:


Cat.columns=['category_id','category_name']


# In[14]:


Cat


# In[15]:


Cat.set_index('category_id', inplace=True)


# In[16]:


Cat


# In[17]:


dct=Cat.to_dict()


# In[18]:


dct['category_name']


# In[19]:


Full_df['category_name']=Full_df['category_id'].map(dct['category_name'])


# In[20]:


Full_df.columns


# In[21]:


Full_df.head(4)


# In[22]:


plt.figure(figsize=(15,10))
sns.boxplot(x="category_name", y="likes", data= Full_df)
plt.xticks(rotation="vertical")


# In[23]:


sns.barplot(x="category_name", y="likes", data=Full_df)
plt.xticks(rotation="vertical")


# In[24]:


new_df= Full_df[["category_name","likes"]]


# In[25]:


new_df=new_df.groupby(['category_name']).sum()


# In[26]:


new_df


# In[27]:


sns.heatmap(new_df)


# # Let's find out whether audiences are engaging or not.

# In[28]:


Full_df.head(4)


# In[29]:


Full_df["likes_rate"]=Full_df["likes"]/Full_df["views"]


# In[30]:


Full_df["dislikes_rate"]=Full_df["likes"]/Full_df["views"]


# In[31]:


Full_df["comments_rate"]=Full_df["comment_count"]/Full_df["views"]


# In[32]:


Engage_df= Full_df[["category_name","likes_rate","dislikes_rate","comments_rate"]]


# In[33]:


Engage_df


# In[34]:


df2 = Engage_df.groupby('category_name')['likes_rate'].sum()


# In[35]:


df2


# In[36]:


Full_df.drop(["likes_rate","dislikes_rate","comments_rate"], axis=1)


# In[37]:


Engage_df= Full_df[["category_name","likes","dislikes","comment_count","views"]]


# In[38]:


Engage_df


# In[39]:


Engage_df= Engage_df.groupby('category_name', as_index=True).sum()


# In[ ]:





# In[40]:


Engage_df["likes_rate"]=(Engage_df["likes"]/Engage_df["views"])*100


# In[41]:


Engage_df


# In[42]:


Engage_df["dislikes_rate"]=(Engage_df["dislikes"]/Engage_df["views"])*100


# In[43]:


Engage_df


# In[44]:


Engage_df["comment_rate"]=(Engage_df["comment_count"]/Engage_df["views"])*100


# In[45]:


Engage_df


# In[49]:


import matplotlib.ticker as mtick
sns.barplot(x=Engage_df.index, y="likes_rate", data= Engage_df)
plt.xticks(rotation="vertical")
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100.0))


# In[50]:


sns.regplot(x="likes",y="views", data=Engage_df)


# In[51]:


sns.heatmap(Full_df[["views","likes","dislikes"]].corr(),annot=True)


# # Which Channel has largest trending Videos?

# In[52]:


Full_df.head()


# In[53]:


cdf=Full_df.groupby("channel_title")["video_id"].count().sort_values(ascending=False).to_frame().reset_index().rename(columns={"video_id":"total_videos"})


# In[54]:


cdf


# In[55]:


import plotly.express as ps


# In[56]:


ps.bar(cdf[0:20], x="channel_title", y="total_videos")


# # Does punctuation in title and tags have the relation with views, likes, dislikes, comments?

# In[57]:


import string


# In[58]:


string.punctuation


# In[65]:


def punc_count(x):
    return len([i for i in x if i in string.punctuation]) 


# In[66]:


Full_df['title'][0]


# In[67]:


punc_count('Eminem - Walk On Water (Audio) ft. BeyoncÃ©')


# In[68]:


sample=Full_df[0:10000]


# In[74]:


sample['punc_count']=sample['title'].apply(punc_count)


# In[75]:


sample.head(2)


# Box plot between the punctuation count and the views shows some sort of statistics.

# In[76]:


sns.boxplot(x='punc_count', y='views', data=sample)


# In[78]:


sample['punc_count'].corr(sample['views'])


# The correlation between the punction count and views is lamost 7%, this doesnot given any big conclusion with respect to their association.

# In[ ]:




