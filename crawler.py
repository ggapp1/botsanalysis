# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import tweepy
import time
import botometer
import data
import unicodedata

consumer_key = 'dB3iaqcrW7WtmZnexrcSfgTgQ'
consumer_secret =  'xcrI84UBGG5zx6OgMnStva6pC6jUyEgdvyWKPNZN6B1sKTLVDE'
access_token = '513768992-3O146BZvenG92zJwoUE6SLZ3nhOTRZZhhOfqMwGo'
access_token_secret = 'DT5qKg73yQXeGIblUgXWYjzVYSeBh8HQFjj7jx6aT8fHo'
mashape_key = "RWoa8U8jiImshcKeqzezdmcSr6M7p1U1plajsnTa1CF4tlKGTh"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#    time.sleep(60)
    
twitter_app_auth = {
    'consumer_key': consumer_key,
    'consumer_secret': consumer_secret,
    'access_token': access_token,
    'access_token_secret': access_token_secret,
  }

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)



a = data.get_bot_hashtag("#Bolsonaro", 1, api, bom)

for user, score in a.iteritems():
	print "\nuser "+str(user)+" is probably a bot, score: "+str(score)



"""
# Check a single account followers by id

followers = data.get_bot_followers("1564722306", api, bom)

for user, score in followers.iteritems():
	print "\nuser "+str(user)+" is probably a bot, score: "+str(score)



for tweet in tweepy.Cursor(api.search,q="#Bolsonaro",count=1,lang="pt", tweet_mode='extended').items():
    #print (tweet.created_at, tweet.text, tweet.user.screen_name)
	print "\n****\n"
	if 'retweeted_status' in dir(tweet):
		text = tweet.retweeted_status.full_text
		print "eh retweet do seguinte usuario: "+str(tweet.retweeted_status.user.screen_name)
   	else:
   		text = tweet.full_text

	nfkd_form = unicodedata.normalize('NFKD', text)
   	only_ascii = nfkd_form.encode('ASCII', 'ignore')
   	print "usuario "+str(tweet.user.screen_name)
   	print only_ascii


"""

