import tweepy
import time
import botometer
import unicodedata

def bot_score(user_id, bom):
	print "\nchecking bot....\n"
	user_score = 0
	try:	
		result = bom.check_account(user_id)
		user_score = result['scores']['universal']
		
	except botometer.NoTimelineError:
		print "user {} has no tweets".format(user_id)
			
	except tweepy.TweepError:
	    print("failed for user {}, probably has protected account").format(user_id)

	print "score "+str(user_score)
	return user_score 


def get_bot_followers(user_id, api, bom):
	# Check a single account followers by id

	ids = []

	for page in tweepy.Cursor(api.followers_ids, user_id=user_id).pages():
		ids.extend(page)

	print "user has {} followers".format(len(ids))
	followers = {}

	for user_id in ids:

		user_score = bot_score(user_id, bom)
		    
		if (user_score > 0.6):
			followers[user_id] = result['scores']['universal']
	
	return followers

def get_bot_hashtag(hashtag, count, api, bom):
	#get bots that are tweeting a especific hashtag

	bots = {}
	i = 0

	for tweet in tweepy.Cursor(api.search,q=hashtag,count=count,lang="pt", tweet_mode='extended').items():
		
		user_score = 0
		reuser_score = 0
		user_id = 0
		reuser_id = 0
		
		if 'retweeted_status' in dir(tweet):

			user_id = 	tweet.user.id
			reuser_id = tweet.retweeted_status.user.id
	
			user_score = bot_score(user_id, bom)
			reuser_score = bot_score(reuser_id, bom)
	
	   	else:
	   		user_id = 	tweet.user.id
			user_score = bot_score(user_id, bom)

		i = i + 1
		print "user "+str(i)

	   	if(user_score > 0.6):
	   		bots[user_id] = user_score
		if(reuser_score > 0.6):
	   		bots[reuser_id] = reuser_score
	return bots

def get_tweets(user_id, api):

	tweet_list = []
	print len(tweet_list)
	print "teste"
	for pages in tweepy.Cursor(api.user_timeline, id=user_id, count=1,include_rts = True,tweet_mode='extended'
		).pages():        
		for tweet in pages:
			tweet_list.append(tweet)
			print len(tweet_list)
	return tweet_list
"""
def get_bot_following(user_id, api, bom):



def get_geo(user_id, api):
"""