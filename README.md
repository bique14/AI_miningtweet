# AI_miningtweet_By_Twitter_API

This is a school project about data mining in Twitter (by Twitter API).

Twitter API : https://developer.twitter.com/en.html


### How to find key and token ?
1. You can find it at https://apps.twitter.com
2. Create your app.
3. Goto "Permissions"
4. Change permissions to "Read and Write"
5. Go to "Keys and access Tokens" tab.
6. Copy "Consumer Key" and "Consumer Secret"
7. Generate your "Access Token" and "Accesss Token Secret" and copy it.
8. Run your code :)

### Post tweet
```python
postTweet('foobar')
```

### Get trend
```python
getTrending(auth)
```
>you can change your location by WOEID in ..
```
api.trends_place(23424960)
```

### Search tweet (recommended hashtag)
```python
searchTweet('#foobar')
```

### Tracking tweet (recommended hashtag)
its include Retweet
```python
trackingTweet('#foobar')
```

