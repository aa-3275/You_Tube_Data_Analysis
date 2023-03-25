#!/usr/bin/env python
# coding: utf-8

# # Sentiment Analysis of YouTube Channel

# #### We are using the Youtube dataset to form some sentiment analysis on top of that.

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


comments=pd.read_csv(r"F:\Python_Data_Analyis_Project\UScomments.csv", error_bad_lines= False)


# In[6]:


comments.head()


# In[7]:


comments.isnull().sum()


# In[8]:


comments.dropna(inplace=True)


# In[9]:


from textblob import TextBlob


# In[10]:


TextBlob('trending 😉').sentiment.polarity


# In[118]:


df=comments


# In[119]:


polarity=[]
for comment in df['comment_text']:
    try:
        polarity.append(TextBlob(comment).sentiment.polarity)
    except:
        polarity.append(0)


# In[120]:


df['polarity']=polarity


# In[121]:


df.head(14)


# Changing positive polarity as 1 and Negative as -1

# In[122]:


comments_positive= df[df["polarity"]==1]
comments_negative=df[df["polarity"]==-1]


# In[123]:


pip install wordcloud


# In[124]:


from wordcloud import WordCloud, STOPWORDS


# In[125]:


comments_negative['comment_text']


# In[126]:


Total_comments=' '.join(comments_negative['comment_text'])


# In[127]:


Total_comments[0:100]


# ### Negative WordCloud Analysis

# In[128]:


wordcloud= WordCloud(stopwords=set(STOPWORDS)).generate(Total_comments)
plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis('off')


# In[129]:


Total_comments2=' '.join(comments_positive['comment_text'])


# ### Positive WordCloud Analysis

# In[130]:


wordcloud= WordCloud(stopwords=set(STOPWORDS)).generate(Total_comments2)
plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis('off')


# ## Emoji Analysis

# In[131]:


# Install a package called Emoji
get_ipython().system('pip install emoji')


# In[132]:


df.head()


# In[133]:


import emoji


# In[134]:


emojies_list=[]


# In[135]:


import emoji
emojis_list = []
for comment in df['comment_text']:
    emojis_list.extend([j for j in comment if emoji.is_emoji(j)])


# In[136]:


emojis_list[0:10]


# ## Conversion of Emojis into its dictionary having frequencies as its value.

# In[137]:


def frequency_dict(emojis_list):
    dict={}
    for char in emojis_list:
        if char in dict:
            dict[char]+=1
        else:
            dict[char]=1
    return dict


# In[138]:


frequency_dict(emojis_list)


# In[139]:


import collections
counter = collections.Counter(frequency_dict(emojis_list))
counter.most_common(10)


# In[148]:


emojis=[counter.most_common(10)[i][0] for i in range (10)]
freq=[counter.most_common(10)[i][1] for i in range (10)] 


# In[156]:


emojis


# In[157]:


freq


# In[151]:


pip install plotly


# In[152]:


import plotly.graph_objs as go


# In[162]:


from plotly.offline import iplot


# In[169]:


trace=go.Bar(x=emojis, y=freq)


# In[170]:


fig = go.Figure(trace)
fig.show()


# In[ ]:




