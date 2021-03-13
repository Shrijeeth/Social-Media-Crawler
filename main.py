import tweepy

API = 'cnIdIOpoZw1t0PpGBvlej03BZ'
API_SECRET = '9VfhArGpfiGuSTxtwy0OH4Lrf8zMzVmVqven1jjICvOpC6QnVV'

TOKEN = '1449131066-ITGeYx7vsWEgnvZyYtVowR1WWDT0cw0er7Jszpi'
TOKEN_SECRET = 'x5mGO6USkZM459htGICoZrC9cDbdbGBqiFhlglOziqBgr'

auth = tweepy.OAuthHandler(API,API_SECRET)
auth.set_access_token(TOKEN,TOKEN_SECRET)

api = tweepy.API(auth)

def tweets(query) :
    tweet = api.search(q=query,count=10,lang='en',tweet_mode='extended',return_type='recent')
    return tweet

if __name__ == '__main__' :
    query = input("Search : ")
    json = tweets(query)
    for tweet in json :
        print("--------------------------------------------------------------------------------")
        print(tweet.full_text)
        print(tweet.created_at)
        print("--------------------------------------------------------------------------------")