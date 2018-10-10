import tweepy
import time
import botometer
import unicodedata
import os

def limit_handler(cursor):
	#deal with timeouts
	print("## limit handler ##")
	while True:
		try:
			yield cursor.next()
		except tweepy.RateLimitError:
			print("Sleeping...")
			time.sleep(15 * 60)


def bot_score(user_id, bom):
	#returns the bot score of an user
	
	print("\nchecking bot....\n")
	print("id " + str(user_id))
	user_score = 0
	try:	
		result = bom.check_account(user_id)
		user_score = result['scores']['universal']
		
	except botometer.NoTimelineError:
		print("failed, user has no tweets")
			
	except tweepy.TweepError:
	    print("failed, user probably has protected account")
	print("score "+str(user_score))
	return user_score 


def get_bot_followers(user_id, api, bom):
	# Check a single account followers by id

	ids = []

	for page in tweepy.Cursor(api.followers_ids, user_id=user_id).pages():
		ids.extend(page)

	print("user has {} followers".format(len(ids)))
	followers = {}

	for user_id in ids:

		user_score = bot_score(user_id, bom)
		    
		if (user_score > 0.6):
			followers[user_id] = result['scores']['universal']
	
	return followers

def get_bots_by_hashtag(hashtag, api, bom):
	#get bots that are tweeting a especific hashtag
	#and save them in a file

	bots_file = open(hashtag+"_bots", "w+")
	bots_file.write("user_id score\n")
	bots_file.flush()
	os.fsync(bots_file.fileno())

	i = 0
	print("searching "+hashtag)
	for tweet in limit_handler(tweepy.Cursor(api.search,q=hashtag, count=3200, timeout=600).items()):
		user_score = 0
		rtuser_score = 0

		if 'retweeted_status' in dir(tweet):
			rtuser_id = tweet.retweeted_status.user.id
			rtuser_score = bot_score(rtuser_id, bom)
	 
			if(rtuser_score > 0.7):
				bots_file.write("{},{}\n".format(rtuser_id, rtuser_score))
				i = i + 1 
				bots_file.flush()
				os.fsync(bots_file.fileno())
		else:
			user_id = tweet.user.id
			user_score = bot_score(user_id, bom)
	 
			if(user_score > 0.7):
				bots_file.flush()
				os.fsync(bots_file.fileno()) 
				i = i + 1

		if(i > 15):
			print("15 bots founded")
			bots_file.close()
			return;

	print("bots founded: "+str(i))      
	bots_file.close() 

def get_tweets(user_id, api):

	tweet_list = []
	for pages in tweepy.Cursor(api.user_timeline, id=user_id, count=1,include_rts = True,tweet_mode='extended'
		).pages():        
		for tweet in pages:
			tweet_list.append(tweet)
	return tweet_list

	
"""
def get_bot_following(user_id, api, bom):



def get_geo(user_id, api):
"""