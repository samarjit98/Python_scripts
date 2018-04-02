import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer

def text_process(text):
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

yelp = pd.read_csv('yelp.csv')
yelp['text length'] = yelp['text'].apply(len)
#print yelp.head()

g = sns.FacetGrid(data=yelp, col='stars')
g.map(plt.hist, 'text length', bins=50)
plt.show()

stars = yelp.groupby('stars').mean()
print stars.corr()
sns.heatmap(data=stars.corr(), annot=True)
plt.show()

yelp_class = yelp[(yelp['stars'] == 1) | (yelp['stars'] == 5)]
X = yelp_class['text']
y = yelp_class['stars']

sample_text = "Hey there! This is a sample review, which happens to contain punctuations."
print text_process(sample_text)

bow_transformer = CountVectorizer(analyzer=text_process).fit(X)
print "bow tranformer"

review_25 = X[24]
print review_25
bow_25 = bow_transformer.transform([review_25])
print bow_25