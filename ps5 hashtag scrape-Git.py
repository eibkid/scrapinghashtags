#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


####API credentials here
consumer_key = 'xxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


# In[3]:


#authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[5]:


hashtags = api.search(q="#xxxxxxxxxxxxxxxx", count= 300, Lang="en", dates = "dates", tweet_mode= "extended")     


# In[15]:


df = pd.DataFrame([tweet.full_text for tweet in posts] , columns= ['Tweets'])


# In[16]:


#function to clean
def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) #removes mentions
    text = re.sub(r'RT[\s]+', '', text) #removes RT
    text = re.sub(r'https?:\/\/\S+', '', text) #removes hyperlink
    
    return text

df['Tweets']= df['Tweets'].apply(cleanTxt)
df.head()


# In[7]:


def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
    return TextBlob(text).sentiment.polarity
df['Subjectvity'] = df['Tweets'].apply(getSubjectivity)
df['Polarity'] = df['Tweets'].apply(getPolarity)


# In[ ]:


#textblob
ScrapedHashTags = ' '.join( [tweets for tweets in df['Tweets']] )

stopwords = set(STOPWORDS)

wordcloud = WordCloud(width = 700, height = 500, random_state = 21, max_font_size = 119, max_words = 100, stopwords = stopwords).generate(ScarpedHashTags)

plt.imshow(wordcloud, interpolation = "bilinear")
plt.axis('off')
plt.show()
plt.tight_layout

