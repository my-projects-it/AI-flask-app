#!/usr/bin/env python
# coding: utf-8

# In[18]:


#get_ipython().system('pip install --upgrade nltk')

import nltk
import os
from sklearn.feature_extraction.text import TfidfVectorizer

# Set a fixed NLTK data path
nltk.data.path.append("/app/nltk_data")  

d = [
    "ShivShakti represents the divine union of Shiva and Shakti.",
    "Shiva is consciousness, and Shakti is energy.",
    "Together, they symbolize balance and creation."
]

v = TfidfVectorizer()
X = v.fit_transform(d)

def search_text(energy):
    qv = v.transform([energy])
    scores = (X * qv.T).toarray()
    bm = d[scores.argmax()]
    return bm

# In[ ]:
