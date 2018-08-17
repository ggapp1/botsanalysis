import tweepy
import time
import botometer

consumer_key = 'dB3iaqcrW7WtmZnexrcSfgTgQ'
consumer_secret =  'xcrI84UBGG5zx6OgMnStva6pC6jUyEgdvyWKPNZN6B1sKTLVDE'
access_token = '513768992-3O146BZvenG92zJwoUE6SLZ3nhOTRZZhhOfqMwGo'
access_token_secret = 'DT5qKg73yQXeGIblUgXWYjzVYSeBh8HQFjj7jx6aT8fHo'
mashape_key = "RWoa8U8jiImshcKeqzezdmcSr6M7p1U1plajsnTa1CF4tlKGTh"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

ids = []

for page in tweepy.Cursor(api.followers_ids, screen_name="ggapp1").pages():
    ids.extend(page)
 #   time.sleep(60)
    
print ids
print len(ids)


twitter_app_auth = {
    'consumer_key': consumer_key,
    'consumer_secret': consumer_secret,
    'access_token': access_token,
    'access_token_secret': access_token_secret,
  }

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

# Check a single account by id
for user_id in ids:
	try:
		result = bom.check_account(user_id)
	except botometer.NoTimelineError:
		print "user {} has no tweets".format(user_id)
	except tweepy.TweepError:
	    print("failed for user {}, probably has protected account").format(user_id)

	print "\n*****\n"+str(user_id)+"\n            "
	print result