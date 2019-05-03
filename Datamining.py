#!/usr/bin/env python
# coding: utf-8

# In[4]:


from nltk.corpus import stopwords


# In[5]:



file='C:/Users/Welcome/Downloads/datamining.txt'
file1=open(file,'rt')
text=file1.read()
file1.close()
print(text[:600])


# In[3]:


#removing urls
import re
text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
print(text)


# In[4]:


#removing numbers
import re
word1=re.sub(r'\d+','',text)
print(word1[:200])


# In[5]:


#split into words by white space
word2=word1.split()
print(word2[:200])


# In[6]:


# remove punctuation from each word
import string
print("Punctuations  in English:\n",string.punctuation)
table = str.maketrans('','',string.punctuation)
stripped =[W.translate(table) for W in word2]
print("\n Removing Puncuations:\n",stripped[:100])


# In[7]:


#Normalizing case
#convert to lower case
print(stripped[:20],"\n")
word3=[word.lower() for word in stripped]
print(word3[:100])


# In[8]:


#removing the stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
word4=[W for W in word3 if not W in stop_words]
print(word4[:100])


# In[9]:


# stemming of words
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed= [porter.stem(word) for word in word4]
print(stemmed[:100])








# In[10]:




print(" ".join(map(str,stemmed)))


# In[11]:


from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
stopwords = set(STOPWORDS)


# In[12]:


def show_wordcloud(stemmed, title = None):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=200,
        max_font_size=40, 
        scale=3,
        random_state=1 # chosen at random by flipping a coin; it was heads
    ).generate(str(stemmed))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title: 
        fig.suptitle(stemmed, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.show()


# In[13]:


show_wordcloud(stemmed)


# In[102]:





# In[98]:





# In[ ]:




