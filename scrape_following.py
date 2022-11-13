import tweepy
from tweepy import Stream
import json
import pandas as pd


#Installation / Access to Twitter account
consumer_key = '926HR9pegOeIWA4sVavXTwftA'
consumer_secret = 'xRpWQwlxYTch240KVndkV8YIvf1BbtH8eQXFGpoeQAmAC125zf'
access_token = '746626504789008384-41M01lwlitpoZjVor1YXtoyqLPhsYlG'
access_token_secret = 'kjYcekVjfkFtgQw9vBHaF67HsM8dPxunnHhZe6SsxK8Lb'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)


#fetching friends
def scrape_following(username):

    users = []
    user = api.get_user(screen_name=username)
    for _id in (tweepy.Cursor(api.get_friend_ids,
                                          screen_name = username).items()):
        users.append(_id)
        
    return pd.DataFrame({"users":users}) 

data = scrape_following('elonmusk')
data.to_csv('ElonFollowing.csv')