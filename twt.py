# -*- coding: utf-8 -*- 
from TwitterAPI import TwitterAPI
import tweepy 
import ssl
import json
import os
import time
import random
from pythainlp.sentiment import sentiment

from pymongo import MongoClient
con = MongoClient('localhost', 27017)
db = con.get_database("demo")
emp = db.tweet_datas

def postTweet(msg):
    r = api.request('statuses/update', {'status': msg})
    print('SUCCESS' if r.status_code == 200 else 'FAILURE')


def searchTweet(keywords):
    chk = os.stat("searchTwt.json").st_size == 0
    r = api.request('search/tweets', {'q': keywords}) # Search by Hashtag only
    print('SUCCESS' if r.status_code == 200 else 'FAILURE')
    dicts_search = []
    proc = []
    for i,item in enumerate(r):
        print(i,item['text']+'\n' if 'text' in item else item)

        date_spilt = item['created_at'].split()
        dict_item_search = {
            "created_at" : date_spilt[0]+' '+date_spilt[1]+' '+date_spilt[2],
            "id" : item['id'],
            "text" : item['text'],
            "hashtag" : item['entities']['hashtags'],
            "user_id" : item['user']['screen_name'],
            "user_name" : item['user']['name'],
            "retweet_count" : item['retweet_count'],
            "fav_count" : item['favorite_count'],
            "sentiment" : sentiment(item['text']),
            "sum":0,
            "pos":0,
            "neg":0,
            "nat":0
        }
        dicts_search.append(dict_item_search)
    
        emp.insert({
            "created_at" : dicts_search[i]['created_at'],
            "id" : dicts_search[i]['id'],
            "text" : dicts_search[i]['text'],
            "hashtag" : dicts_search[i]['hashtag'],
            "user_id" : dicts_search[i]['user_id'],
            "user_name" : dicts_search[i]['user_name'],
            "retweet_count" : dicts_search[i]['retweet_count'],
            "fav_count" : dicts_search[i]['fav_count'],
            "sentiment" : sentiment(item['text']),
            "sum":0,
            "pos":0,
            "neg":0,
            "nat":0
        })
        
    with open('searchTwt.json', 'w') as outfile:
        json.dump(dicts_search, outfile, ensure_ascii=False)


def trackingTweet(hashtag):
    r = api.request('statuses/filter', {'track': hashtag}) # Track by Hashtag only
    print('SUCCESS' if r.status_code == 200 else 'FAILURE')
    dicts_track = []
    for i,item in enumerate(r):
        print(i,item['text'] if 'text' in item else item)
        print(item['created_at'])

        date_spilt = item['created_at'].split()
        dict_item_track = {
            "created_at" : date_spilt[0]+' '+date_spilt[1]+' '+date_spilt[2],
            "id" : item['id'],
            "text" : item['text'],
            "hashtag" : item['entities']['hashtags'],
            "user_id" : item['user']['screen_name'],
            "user_name" : item['user']['name'],
            "retweet_count" : item['retweet_count'],
            "fav_count" : item['favorite_count'],
            "sentiment" : sentiment(item['text']),
            "sum":0,
            "pos":0,
            "neg":0,
            "nat":0
        }

        dicts_track.append(dict_item_track)
        emp.insert({
            "created_at" : dicts_track[i]['created_at'],
            "id" : dicts_track[i]['id'],
            "text" : dicts_track[i]['text'],
            "hashtag" : dicts_track[i]['hashtag'],
            "user_id" : dicts_track[i]['user_id'],
            "user_name" : dicts_track[i]['user_name'],
            "retweet_count" : dicts_track[i]['retweet_count'],
            "fav_count" : dicts_track[i]['fav_count'],
            "sentiment" : sentiment(item['text']),
            "sum":0,
            "pos":0,
            "neg":0,
            "nat":0
        })
        
        with open('trackTwt.json', 'w') as outfile:
            json.dump(dicts_track, outfile, ensure_ascii=False)
        
        time.sleep(2)

def getTrending(auth):
    api = tweepy.API(auth)
    trends1 = api.trends_place(23424960)
    trends = set([trend['name'] for trend in trends1[0]['trends']])
    list_trends = list(trends)
    show_trends = '\n'.join(trends)
    print(show_trends)
    # print(list_trends)

ssl._create_default_https_context = ssl._create_unverified_context

payloads = {
    'consumer_key' : 'x',
    'consumer_secret' : 'x',
    'access_token_key' : 'x',
    'access_token_secret' : 'x'
}

# TwitterAPI : search, tracking, post
api = TwitterAPI(payloads['consumer_key'], payloads['consumer_secret'], payloads['access_token_key'], payloads['access_token_secret'])

# Tweepy : Get Trending
auth = tweepy.OAuthHandler(payloads['consumer_key'], payloads['consumer_secret'])
auth.set_access_token(payloads['access_token_key'], payloads['access_token_secret'])


# TEST 
find_hashtag = ['#มธ', '#ธรรมศาสตร์', '#ทีมมธ','#admission61','#admission']
# getTrending(auth)
for i in range(len(find_hashtag)):
    searchTweet(find_hashtag[i])
# trackingTweet('#มธ')
