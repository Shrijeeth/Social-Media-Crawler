import tweepy
import re
from nltk.stem import PorterStemmer
import sentiment_model
import io

f = open('api.txt')
l = f.readlines()
API = l[1][:-1]
API_SECRET = l[3][:-1]
TOKEN = l[5][:-1]
TOKEN_SECRET = l[7][:-1]
f.close()

auth = tweepy.OAuthHandler(API,API_SECRET)
auth.set_access_token(TOKEN,TOKEN_SECRET)

api = tweepy.API(auth)

model,stem,pp,maxlen = sentiment_model.load_model()
ps = PorterStemmer()

def preprocess(content,stem=True) :
    regex = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
    content = re.sub(regex,' ', str(content).lower()).strip()
    tokens = []
    for token in content.split():
        if stem :
            tokens.append(ps.stem(token))
        else :
            tokens.append(token)
    return " ".join(tokens)

def tweets(query) :
    tweet = api.search(q=query+" -filter:retweets",count=100,lang='en',tweet_mode='extended',return_type='recent')
    return tweet

def prediction(content) :
    if pp :
        word_array = sentiment_model.get_word_array(content,maxlen)
    else :
        word_array = [content]
    pred = model.predict(word_array)
    return pred

def search(query) :
    positive = neutral = negative = overall = 0
    json = tweets(query.lower())
    f = io.open('tweet.txt','w',encoding='utf-8')
    for tweet in json :
        if pp :
            txt = preprocess(tweet.full_text,stem)
        else :
            txt = tweet.full_text
        score = prediction(txt)[0][0]
        f.write("\n\n--------------------------------------------------------------------------------\n\n")
        f.write(str(tweet.full_text) + '\t')
        f.write(str(tweet.created_at) + '\t')
        f.write(f"Sentiment Score : {score}\t")
        f.write("\n\n--------------------------------------------------------------------------------\n\n")
        overall += score 
        if (score > 0.7) and (score <= 1) :
            positive += 1
        elif (score < 0.3) and (score >= 0) :
            negative += 1
        else :
            neutral += 1
    f.close()
    overall /= (positive + negative + neutral)
    return positive,negative,neutral,overall