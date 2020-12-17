#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:43:12 2020

@author: client-10
"""

import tweepy
import pandas as pd


consumer_key = '63b65EOO8kVomwTHuI86LQBKF'
consumer_secret = 'LfroxSmhFZFsCVDRI37MQxfw9Fo2OIiyTCV5dbt6zpFWQBgA5y'
access_token = '1163688140755783680-DnAWGATrIyMpF45yREyf77mM4L1TUr'
access_token_secret = 'VKhGApNavguQPwLn5mBWyaKQlk87W4Y73bD18AmBmteGo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("63b65EOO8kVomwTHuI86LQBKF", "LfroxSmhFZFsCVDRI37MQxfw9Fo2OIiyTCV5dbt6zpFWQBgA5y")
auth.set_access_token("1163688140755783680-DnAWGATrIyMpF45yREyf77mM4L1TUr", "VKhGApNavguQPwLn5mBWyaKQlk87W4Y73bD18AmBmteGo")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit = True,
    wait_on_rate_limit_notify = True)

timeline = api.home_timeline()

for tweet in timeline:
    print(tweet.user.name)

api.update_status("Test tweet from Tweepy Python")
user = api.get_user("MikezGarcia")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

tweets = api.home_timeline(count = 1)
tweet = tweets[0]
print(tweet.id)
api.create_favorite(tweet.id)

tweets = api.mentions_timeline()
for tweet in tweets:
    print(tweet.favorite())
    print(tweet.retweet())


#world trend list
world_trends = api.trends_available()

df= pd.DataFrame(world_trends)

df.to_csv('/home/client-10/Videos/world_tren1.csv', encoding = 'utf-8', index = False)

dd=pd.read_csv("/home/client-10/Documents/city.csv")

name = 'Albuquerque'

df1 = dd[dd.cityname == name]

df2 = df1['Weoid']

df2 = int(df2)

place = api.trends_place(df2)

total = place[0]
print(total)

split = total["trends"]

mm=pd.DataFrame(split)

mm.to_csv('/home/client-10/Videos/tweet/mm1.csv', encoding = 'utf-8', index = False)

# Tweets details Part

single = split[3]
print(single)

mm=pd.DataFrame(single.items())
print(mm)

trenddata = pd.DataFrame(mm, columns = ['name', 'tweet_volume'])
print(trenddata)

row = mm.iloc [[3,2],]
print(row)

tr = row.transpose()

header = tr.iloc[0]
tr = tr[1:]
value=tr.rename(columns = header)

t1 = list(set(value.name))
t2=  list(set(value.tweet_volume))
             
dy = api.search(q = t1, lang = 'en' ,count = 200,result_type = "recent")

   
df = pd.DataFrame(columns = ['text', 'source', 'url','count','created'])

msgs = []
msg =[]

for tweet in tweepy.Cursor(api.search, q = t1, rpp = 100).items(100):
    msg = [df.columns, tweet.text, tweet.source, tweet.source_url, tweet.retweet_count, tweet.created_at, tweet.favourites_count]
    msg = tuple(msg)                    
    msgs.append(msg)
    
msgs

final = pd.DataFrame(msgs)

final.to_csv('/home/client-10/Videos/tweet/trending_detal.csv', encoding = 'utf-8', index = False)

