from TwitterAPI import TwitterAPI
import tweepy 
import ssl
import json
import os

from pymongo import MongoClient
con = MongoClient('localhost', 27017)
db = con.get_database("demo")
emp = db.tweet_data

def postTweet(msg):
    r = api.request('statuses/update', {'status': msg})
    print('SUCCESS' if r.status_code == 200 else 'FAILURE')


def searchTweet(keywords):
    chk = os.stat("searchTwt.json").st_size == 0
    r = api.request('search/tweets', {'q': keywords}) # Search by Hashtag only
    print('SUCCESS' if r.status_code == 200 else 'FAILURE')
    dicts_search = []
    for i,item in enumerate(r):
        print(i,item['text']+'\n' if 'text' in item else item)
        dicts_search.append(item)
        emp.insert({
            "created_at" : dicts_search[i]['created_at'],
            "id" : dicts_search[i]['id'],
            "text" : dicts_search[i]['text'],
            "hashtag" : dicts_search[i]['entities']['hashtags'],
            "user_id" : dicts_search[i]['user']['screen_name'],
            "user_name" : dicts_search[i]['user']['name'],
            "retweet_count" : dicts_search[i]['retweet_count'],
            "fav_count" : dicts_search[i]['favorite_count']
        })
    
    with open('searchTwt.json', 'w') as outfile:
        json.dump(dicts_search, outfile, ensure_ascii=False)


def trackingTweet(hashtag):
    r = api.request('statuses/filter', {'track': hashtag}) # Track by Hashtag only
    print('SUCCESS' if r.status_code == 200 else 'FAILURE')
    dicts_track = []
    for i,item in enumerate(r):
        print(i,item['text'] if 'text' in item else item)
        dicts_track.append(item)
        emp.insert({
            "created_at" : dicts_track[i]['created_at'],
            "id" : dicts_track[i]['id'],
            "text" : dicts_track[i]['text'],
            "hashtag" : dicts_track[i]['entities']['hashtags'],
            "user_id" : dicts_track[i]['user']['screen_name'],
            "user_name" : dicts_track[i]['user']['name'],
            "retweet_count" : dicts_track[i]['retweet_count'],
            "fav_count" : dicts_track[i]['favorite_count']
        })



        with open('trackTwt.json', 'w') as outfile:
            json.dump(dicts_track, outfile, ensure_ascii=False)

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
    'consumer_key' : 'fzxvRuTrMvFrGOsULifyGUJyC',
    'consumer_secret' : 'nuwjhfDZPMyRSK42gzxKi8rhqohON3dvo5NBQVIxcV0pBPlnSo',
    'access_token_key' : '970858119394807808-IgFxFXUIZRMxEDlPxwNBzSb72x1NJx4',
    'access_token_secret' : 'JlUEodSz2Pb0mflS2uE5LIfgFfKlL9yaJWoz3aM83x6Xk'
}

# TwitterAPI : search, tracking, post
api = TwitterAPI(payloads['consumer_key'], payloads['consumer_secret'], payloads['access_token_key'], payloads['access_token_secret'])

# Tweepy : Get Trending
auth = tweepy.OAuthHandler(payloads['consumer_key'], payloads['consumer_secret'])
auth.set_access_token(payloads['access_token_key'], payloads['access_token_secret'])


# TEST 
# getTrending(auth)
# searchTweet('#บุพเพสันนิวาส')
trackingTweet('#บุพเพสันนิวาส')

