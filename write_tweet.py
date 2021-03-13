import tweepy
import json

API = 'cnIdIOpoZw1t0PpGBvlej03BZ'
API_SECRET = '9VfhArGpfiGuSTxtwy0OH4Lrf8zMzVmVqven1jjICvOpC6QnVV'

TOKEN = '1449131066-ITGeYx7vsWEgnvZyYtVowR1WWDT0cw0er7Jszpi'
TOKEN_SECRET = 'x5mGO6USkZM459htGICoZrC9cDbdbGBqiFhlglOziqBgr'

auth = tweepy.OAuthHandler(API,API_SECRET)
auth.set_access_token(TOKEN,TOKEN_SECRET)

api = tweepy.API(auth)

tweet_list=[]

class MyStreamListener(tweepy.StreamListener):
    def __init__(self,api=None):
        super(MyStreamListener,self).__init__()
        self.num_tweets=0
        self.file=open("tweet.txt","w")
    def on_status(self,status):
        tweet=status._json
        self.file.write(json.dumps(tweet)+ '\n')
        tweet_list.append(status)
        self.num_tweets+=1
        if self.num_tweets<10:
            return True
        else:
            return False
        self.file.close()

l = MyStreamListener()
stream = tweepy.Stream(auth,l,tweet_mode='extended',lang='en')
keywords = list(input("Enter Keywords related to your search : ").split())
stream.filter(track=keywords)