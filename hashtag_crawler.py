# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import tweepy
import time
import botometer
import data
import unicodedata

consumer_key = 'tWKbAjFMDKB2vT5pvm5CH3HkB'
consumer_secret= 'hf5UIPFJymZ6XtYDqdNq7LVfLEztcsvRrW1ZLwbF8jzMHV0AXG'
access_token = '513768992-JfWa1xMpBFKQNWfHlUncCVDCPxDOUVs8shUegVQU'
access_token_secret= 'tRQcBExN1vG6otAZnM0L2QHyUupM2qJIz04wcFqkCYoVY'

"""
consumer_key = 'dB3iaqcrW7WtmZnexrcSfgTgQ'
consumer_secret =  'xcrI84UBGG5zx6OgMnStva6pC6jUyEgdvyWKPNZN6B1sKTLVDE'
access_token = '513768992-3O146BZvenG92zJwoUE6SLZ3nhOTRZZhhOfqMwGo'
access_token_secret = 'DT5qKg73yQXeGIblUgXWYjzVYSeBh8HQFjj7jx6aT8fHo'
"""
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

#bom = botometer.Botometer(wait_on_ratelimit=True,
#                          mashape_key=mashape_key,
#                          **twitter_app_auth)

users = [1020798087449776128,
67150902,
58930813,
4896510833,
73995962,
1042201567695396864,
25761099,
1444645189,
34366699,
77641038,
1020798087449776128,
139219536,
250783433,
47754867,
327715048,
42914158,
462832634,
67150902,
4896510833,
179753394,
1042201567695396864,
139219536,
1009248581189033984,
75270377,
67150902,
2505521406,
4060086012,
1020798087449776128,
14594813,
34366699,
41213062,
527049338,
45191045,
1020798087449776128,
14594813,
1042201567695396864,
139219536,
14594813,
824976268546408448,
67150902,
34366699,
30857469,
788794760764985344,
201867844,
16909667,
14594813,
331218846,
75270377,
14594813,
139219536,
1020798087449776128,
709371326822277121,
1042201567695396864,
1258012146,
794866608,
2493175040,
14594813,
67150902,
14594813,
34261231,
139219536,
67150902,
14594813,
139219536,
14594813,
1042201567695396864,
57138606,
75270377,
1042201567695396864,
1020798087449776128,
8802752,
3175,
139219536,
14594813,
1020798087449776128]
for user in users:
  f = open("files/tweets_"+str(user), "w+")
  print("got")
  tweets = data.get_tweets(user, api)
  for tweet in tweets:
    if 'retweeted_status' in dir(tweet):
      text = tweet.retweeted_status.full_text
    else:
      text = tweet.full_text
    nfkd_form = unicodedata.normalize('NFKD', text)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')    
    f.write(str(only_ascii.decode('utf-8'))+"\n")
    f.flush()
  f.close()

#get net of haddad and bolso
#users = [354095556, 128372940]
"""
hashtags = ["#DebateSBT"]


for hashtag in hashtags:
  data.get_bots_by_hashtag(hashtag, api, bom)


"""

"""
a = data.get_bot_hashtag("#Bolsonaro", 1, api, bom)

for user, score in a.iteritems():
	print "\nuser "+str(user)+" is probably a bot, score: "+str(score)




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

