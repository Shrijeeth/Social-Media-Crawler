import tweepy
import json

API = 'cnIdIOpoZw1t0PpGBvlej03BZ'
API_SECRET = '9VfhArGpfiGuSTxtwy0OH4Lrf8zMzVmVqven1jjICvOpC6QnVV'

TOKEN = '1449131066-ITGeYx7vsWEgnvZyYtVowR1WWDT0cw0er7Jszpi'
TOKEN_SECRET = 'x5mGO6USkZM459htGICoZrC9cDbdbGBqiFhlglOziqBgr'

auth = tweepy.OAuthHandler(API,API_SECRET)
auth.set_access_token(TOKEN,TOKEN_SECRET)

api = tweepy.API(auth)

tweets_data_path='tweet.txt'
tweets_data=[]
tweets_file=open(tweets_data_path,"r")

for line in tweets_file:
    tweet=json.loads(line)
    tweets_data.append(tweet)
tweets_file.close()

for i in tweets_data :
    print('------------------------------------------------------------------------------------')
    try :
        print(i['retweeted_status']['extended_tweet']['full_text'])
    except KeyError :
        print(i['text'])
    print('------------------------------------------------------------------------------------')