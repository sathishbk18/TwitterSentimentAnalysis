#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:37:18 2020

@author: client-10
"""

from IPython import display

from pprint import pprint
import pandas as pd
import numpy as np
import nltk
import re
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []

dd=pd.read_csv('/home/client-10/Documents/Mohana/Files/Final4.csv')

def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
        
    return input_txt

dd['Clean_text'] = np.vectorize(remove_pattern)(dd['comments'], "@[\w]*")

dd['Clean_text'] = dd['Clean_text'].str.replace("[^a-zA-Z#]", " ")

dd['Clean_text'] = dd['Clean_text'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))

tokenized_tweet = dd['Clean_text'].apply(lambda x: x.split())

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

tokenized_tweet = tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x]) # stemming
tokenized_tweet.head()

for i in range(len(tokenized_tweet)):
    tokenized_tweet[i] = ' '.join(tokenized_tweet[i])

tokenized_tweet

dd['Clean_text'] = tokenized_tweet
dd['Clean_text'].tail()

dd.drop(['neg', 'pos', 'neu'], axis = 1)
dd.to_csv('/home/client-10/Documents/Mohana/Files/SentimentAnalysis/gg.csv', index = False)

line="RT @choo_ek: Please help combat xenophobia: 1. Don't call COVID-19 Chinese coronavirus or the Wuhan virus 2. Don't shun Asian people or…"
pol_score = sia.polarity_scores(line)
pol_score 
pol_score['comments'] = line
results.append(pol_score)
results   
 
studentData = {
    'Clean_Text' : tokenized_tweet
}
k=pd.DataFrame(studentData)
k.head()
k.to_csv('/home/client-10/Documents/Mohana/Files/SentimentAnalysis/gg.csv',index=False)

for line in tokenized_tweet:
    pol_score = sia.polarity_scores(line)
    results.append(pol_score)
    
    
pprint(results[:3], width = 100)

df = pd.DataFrame.from_records(results)
df.head()

df['Result'] = 0
df.loc[df['compound'] > 0.2, 'Result'] = 1
df.loc[df['compound'] < -0.2, 'Result'] = -1
df.head()


df = df[['compound', 'neg', 'neu', 'pos', 'Result']]

ss = df.drop(['compound'], axis = 1)
ss = {"df":[]} 

ss = df.drop(['compound'], axis = 1)
ss

#save the headlines in csv format
ss.to_csv('/home/client-10/Documents/Mohana/Files/SentimentAnalysis/Analysis12.csv', mode = 'a', encoding = 'utf-8', header = True, index = False)
dd['neg'] = ss['neg']
dd['pos'] = ss['pos']
dd['neu'] = ss['neu'] 

dd.to_csv('/home/client-10/Documents/Mohana/Files/SentimentAnalysis/Output10.csv', index = False)