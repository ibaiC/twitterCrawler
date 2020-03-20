import tweepy
import json
import pymongo
import time
from datetime import datetime

# import oauth2 as oauth
auth = tweepy.OAuthHandler("01GoAHqiLgFvbBEgQPTDFHjBW", "69C7UQ0J6PA604kYbUxMxBkZCaQu786kj6XlhEv1d0TDo1UxYK")
auth.set_access_token("1233433156101005312-vD2zl5VPgH8kFjnl1zRRuN3ed7YfSA", "jbmc1cDwdz5Z0WGZeFw10riX8t4IkvKn1y9jrGJf4JKHf")
api = tweepy.API(auth)

# MongoDB setup
client = pymongo.MongoClient('127.0.0.1',27017) 
db = client.twitterCrawl
collection = db["tweets"]

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # username = status.user.screen_name
        # text = status.text.strip()
        # date = status.created_at
        # _id = status.id
        # hashtags_dict = status.entities["hashtags"]
        # hashtags = []
        # for tag in hashtags_dict:
        #     hashtags.append(tag["text"])
        
        # mentions_dict = status.entities["user_mentions"]
        # mentions = []
        # for user in mentions_dict:
        #     mentions.append(user["screen_name"])

        # # Add tweet to database
        # tweetDocument = {"text": text, "id": _id, "date": date, "username": username, "hashtags": hashtags, "mentions": mentions }
        # insertion = collection.insert_one(tweetDocument)
        tweet = status._json
        collection.insert_one(tweet)


# REST API calls
rest = api.search("coronavirus", lang=["en"])

for item in rest:
#     username = item._json["user"]["screen_name"]
#     text = item._json["text"]
#     date = item._json["created_at"]
#     _id = item._json["id"]

#     hashtags_dict = item._json["entities"]["hashtags"]
#     hashtags = []
#     for tag in hashtags_dict:
#         hashtags.append(tag["text"])

#     mentions_dict = item._json["entities"]["user_mentions"]
#     mentions = []
#     for user in mentions_dict:
#         mentions.append(user["screen_name"])
    

#     #parse date
#     created = datetime.strptime(date, '%a %b %d %H:%M:%S +0000 %Y')

#     tweetDoc = {  "text": text, "id": _id, "date": created, "username": username, "hashtags": hashtags, "mentions": mentions }
#     insertion = collection.insert_one(tweetDoc)
    insertion = collection.insert_one(item._json)



# Streaming API calls
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['coronavirus'], languages=["en"])