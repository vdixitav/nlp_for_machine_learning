# -*- coding: utf-8 -*-
"""Bag of Words Practicals.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TNhm28Oe9VLRcO1ntKwCKeBc7BWprrnc
"""

import pandas as pd

messeges = pd.read_csv("/content/spam.csv", sep='\t', names=['label', 'message'], encoding='latin-1')

messeges

#Data cleaning and reprocessing

import re
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

messeges = pd.read_csv("/content/spam.csv", sep='\t', names=['label', 'message'], encoding='latin-1')

corpus=[]
for i in range(0, len(messeges)):
  # Decode the message to a string if it's bytes, handle it as a string otherwise
  if isinstance(messeges['message'][i], bytes):
    review = re.sub('[^a-zA-Z]', ' ', messeges['message'][i].decode('utf-8', errors='replace'))  # Handle potential decoding errors
  else:
    review = re.sub('[^a-zA-Z]', ' ', str(messeges['message'][i])) # Convert to string before applying regex

  # Continue processing the review (now guaranteed to be a string)
  review = review.lower()
  review = review.split()
  review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
  review = ' '.join(review)
  corpus.append(review)

corpus

# create bag of words
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=2500)
X = cv.fit_transform(corpus).toarray()

X.shape

X

