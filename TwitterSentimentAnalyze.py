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

nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []

dd=pd.read_csv('/home/client-10/Documents/Mohana/Files/Final4.csv')


for line in dd['comments']:
    pol_score = sia.polarity_scores(line)
    results.append(pol_score)
    
    
pprint(results[:3], width = 100)

df = pd.DataFrame.from_records(results)
df.head()

#save the headlines in csv format
df.to_csv('/home/client-10/Documents/Mohana/Files/SentimentAnalysis/Analysis12.csv', mode = 'a', encoding = 'utf-8', header = True, index = False)
dd['neg'] = df['neg']
dd['pos'] = df['pos']
dd['neu'] = df['neu'] 

dd.to_csv('/home/client-10/Documents/Mohana/Files/SentimentAnalysis/Output10.csv', index = False)