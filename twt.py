from TwitterAPI import TwitterAPI
import tweepy 
import ssl
import json
import os

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

    with open('searchTwt.json', 'w') as outfile:
        json.dump(dicts_search, outfile, ensure_ascii=False)


def trackingTweet(hashtag):
    r = api.request('statuses/filter', {'track': hashtag}) # Track by Hashtag only
    print('SUCCESS' if r.status_code == 200 else 'FAILURE')
    dicts_track = []
    for i,item in enumerate(r):
        print(i,item['text'] if 'text' in item else item)
        dicts_track.append(item)
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
    'consumer_key' : 'xxxx',
    'consumer_secret' : 'xxx',
    'access_token_key' : 'xxxx',
    'access_token_secret' : 'xxxx'
}

# TwitterAPI : search, tracking, post
api = TwitterAPI(payloads['consumer_key'], payloads['consumer_secret'], payloads['access_token_key'], payloads['access_token_secret'])

# Tweepy : Get Trending
auth = tweepy.OAuthHandler(payloads['consumer_key'], payloads['consumer_secret'])
auth.set_access_token(payloads['access_token_key'], payloads['access_token_secret'])


# TEST 
# getTrending(auth)
# searchTweet('#บุพเพสันนิวาส')
# trackingTweet('#บุพเพสันนิวาส')

