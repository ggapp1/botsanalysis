import tweepy
import time
import botometer




def get_bot_followers(user_id, api, bom):
	# Check a single account followers by id

	ids = []

	for page in tweepy.Cursor(api.followers_ids, user_id=user_id).pages():
		ids.extend(page)

	print "user has {} followers".format(len(ids))
	followers = {}

	for user_id in ids:

		user_score = 0
		try:
			result = bom.check_account(user_id)
			user_score = result['scores']['universal']
		
		except botometer.NoTimelineError:
			print "user {} has no tweets".format(user_id)
			
		except tweepy.TweepError:
		    print("failed for user {}, probably has protected account").format(user_id)
		    
		if (user_score > 0.6):
			followers[user_id] = result['scores']['universal']
	
	return followers
"""
def get_bot_hashtag(hashtag, api, bom):
	for tweet in tweepy.Cursor(api.search,q=hashtag,count=1,lang="pt").items():
		print (tweet.created_at, tweet.text, tweet.user.screen_name)



def get_bot_following(user_id, api, bom):

def get_tweets(user_id, api):

def get_geo(user_id, api):
"""