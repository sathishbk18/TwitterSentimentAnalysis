#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:33:05 2020

@author: client-10
"""

from requests_oauthlib import OAuth1Session
import pandas as pd
import json

consumer_key = 'aVBh05cj6e2qn5nul3WIZwr8W'  # Add your API key here
consumer_secret = 'RHPxWJHZQxcMEBgWAiyUvdZ3HCiRWXoe8rhQmhNufuqVx9fQC7'  # Add your API secret key here

params = {"ids": "1232731433145421825", "tweet.fields": "created_at"}

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token"
oauth = OAuth1Session(consumer_key, client_secret = consumer_secret)
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')
print("Got OAuth token: %s" % resource_owner_key)

# # Get authorization
base_authorization_url = 'https://api.twitter.com/oauth/authorize'
authorization_url = oauth.authorization_url(base_authorization_url)
print('Please go here and authorize: %s' % authorization_url)
#https://api.twitter.com/oauth/authorize?oauth_token=Z6TkEQAAAAABCvJbAAABcIpuIvc
verifier = '6443571'

# # Get the access token
access_token_url = 'https://api.twitter.com/oauth/access_token'
oauth = OAuth1Session(consumer_key,
                     client_secret = consumer_secret,
                     resource_owner_key = resource_owner_key,
                     resource_owner_secret = resource_owner_secret,
                     verifier = verifier)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens['oauth_token']
access_token_secret = oauth_tokens['oauth_token_secret']

# Make the request
oauth = OAuth1Session(consumer_key,
                       client_secret = consumer_secret,
                       resource_owner_key = access_token,
                       resource_owner_secret = access_token_secret)

# Retweet and favourites of multiples queries

query = []
retweet_count = []
favourites_count = []
comments = []
nn=pd.read_csv('/home/client-10/Documents/Mohana/Files/City39.csv')

for j in nn['query']:
    response = oauth.get("https://api.twitter.com/1.1/search/tweets.json?q={}".format(j), params = params)
    todos = json.loads(response.text)
    todos == response.json()
    print('query:',j)
    for k in range(0,7):
        query.append(j)
        # print('range:',k)
        c = todos['statuses'][k]['retweet_count']
        # print('c=',c)
        retweet_count.append(c)
        
        d = todos['statuses'][k]['user']['favourites_count']
        # print('d=',d)
        favourites_count.append(d)
        
        e = todos['statuses'][k]['text']
        # print('e=',e)
        comments.append(e)  
        
mm= pd.DataFrame(columns=['query','retweet_count','favourites_count','comments'])

        
mm['query'] = query
mm['retweet_count'] = retweet_count
mm['favourites_count'] = favourites_count
mm['comments'] = comments
city = 'NewYork'
city       
mm.insert(0, 'cityname', city)
mm
mm.to_csv('/home/client-10/Documents/Mohana/Files/queries39.csv', encoding = 'utf-8', index = False)
     
print('retweet_count of multiple query:', retweet_count)
print('favourites_count of multiple query:', favourites_count)
print('comments of multiple query:', comments)