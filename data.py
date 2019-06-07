import tweepy
import time
import botometer
import unicodedata
import os
import time

def generate_API():
	consumer_key = 'tWKbAjFMDKB2vT5pvm5CH3HkB'
	consumer_secret= 'hf5UIPFJymZ6XtYDqdNq7LVfLEztcsvRrW1ZLwbF8jzMHV0AXG'
	access_token = '513768992-JfWa1xMpBFKQNWfHlUncCVDCPxDOUVs8shUegVQU'
	access_token_secret= 'tRQcBExN1vG6otAZnM0L2QHyUupM2qJIz04wcFqkCYoVY'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
	
	return api

def generate_Botometer():	
	consumer_key = 'tWKbAjFMDKB2vT5pvm5CH3HkB'
	consumer_secret= 'hf5UIPFJymZ6XtYDqdNq7LVfLEztcsvRrW1ZLwbF8jzMHV0AXG'
	access_token = '513768992-JfWa1xMpBFKQNWfHlUncCVDCPxDOUVs8shUegVQU'
	access_token_secret= 'tRQcBExN1vG6otAZnM0L2QHyUupM2qJIz04wcFqkCYoVY'

	mashape_key = "RWoa8U8jiImshcKeqzezdmcSr6M7p1U1plajsnTa1CF4tlKGTh"
	twitter_app_auth = {
    'consumer_key': consumer_key,
    'consumer_secret': consumer_secret,
    'access_token': access_token,
    'access_token_secret': access_token_secret,
  	}

	bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)
	return bom

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

	user_score = 0
	try:	
		result = bom.check_account(user_id)
		user_score = result['scores']['universal']
		
	except botometer.NoTimelineError:
		print("failed, user has no tweets")
			
	except tweepy.TweepError:
	    print("failed, user probably has protected account")

	return user_score 

def get_followers(user_id, api):
	# return account followers by id
	ids = []
	sleeptime = 5  
	pages = tweepy.Cursor(api.followers_ids, user_id=user_id, timeout=600).pages()
	while True:
	    try:
	        page = next(pages)
	        for tweet in page:
	        	ids.append(tweet)
	        time.sleep(sleeptime)

	    except tweepy.TweepError as e: #taking extra care of the "rate limit exceeded"
	        print(e.api_code)
	        time.sleep(60) 
	        try:
	        	page = next(pages)
	        except tweepy.TweepError as e:
	        	print(e.api_code)
	        	print("failed, user probably has protected account")
	   	    	print(user_id)
	   	    	return ids

	    except StopIteration:
	        break
		
	    if(len(ids) >= 10000):
		    print("user has {} followers".format(len(ids)))
		    return ids
	"""
	for page in limit_handler(tweepy.Cursor(api.followers_ids, user_id=user_id, timeout=600).pages()):
		ids.extend(page)
	"""
	print("user has {} followers".format(len(ids)))
	return ids

def get_bot_followers(user_id, api, bom):
	# Check a single account followers by id

	ids = []

	for page in tweepy.Cursor(api.followers_ids, user_id=user_id).pages():
		ids.extend(page)

	print("user has {} followers".format(len(ids)))
	followers = {}

	for user_id in ids:

		user_score = bot_score(user_id, bom)
		    
		if (user_score > 0.7):
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
#			rtuser_score = bot_score(rtuser_id, bom)
	 
	#		if(rtuser_score > 0.7):
			bots_file.write("{},{}\n".format(rtuser_id, rtuser_score))
			i = i + 1 
			bots_file.flush()
			os.fsync(bots_file.fileno())
		else:
			user_id = tweet.user.id
#			user_score = bot_score(user_id, bom)
	 
#			if(user_score > 0.7):
			bots_file.write("{},{}\n".format(user_id, user_score))
			bots_file.flush()
			os.fsync(bots_file.fileno()) 
			i = i + 1

		if(i > 100000):
			print("enough")
			bots_file.close()
			return;

	print("bots founded: "+str(i))      
	bots_file.close() 

def get_tweets(user_id, api):
	print("- Getting tweets...")
	tweets = [[]]
	tweet_list = []
	tweet_text = []
	pages = tweepy.Cursor(api.user_timeline, id=user_id, count=200,timeout=600,lsinclude_rts = False,tweet_mode='extended'
	).pages()  
	sleeptime = 5
	while True:
	    try:
	        page = next(pages)
	        for tweet in page:
	        	tweet_list.append(tweet)
	        time.sleep(sleeptime)

	    except tweepy.TweepError as e: #taking extra care of the "rate limit exceeded"
	        print(e.api_code)
	        time.sleep(60) 
	        try:
	        	page = next(pages)
	        	for tweet in page:
	        		tweet_list.append(tweet)
	        		time.sleep(sleeptime)

	        except tweepy.TweepError as e:
	            print(e.api_code)
	            print("failed, user probably has protected account")
	            print(user_id)
	            break
	    except StopIteration:
	        break
	"""

	for pages in tweepy.Cursor(api.user_timeline, id=user_id, count=200,timeout=600,lsinclude_rts = False,tweet_mode='extended'
		).pages():        
		for tweet in pages:
			tweet_list.append(tweet)
	"""
	print("len "+str(len(tweet_list)))

	for tweet in tweet_list:	
	  if 'retweeted_status' in dir(tweet):
	    text = tweet.retweeted_status.full_text
	    created_at = tweet.retweeted_status.created_at
	    favs = tweet.retweeted_status.favorite_count
	    retweets = tweet.retweeted_status.retweet_count

	    if tweet.retweeted_status.entities['hashtags']:
	    	hashtags = tweet.retweeted_status.entities['hashtags'][0]['text']
	    else:
	    	hashtags = ""

	    if tweet.retweeted_status.entities['urls']:
	    	url = tweet.retweeted_status.entities['urls'][0]['expanded_url']
	    else:
	    	url = ""

	    is_retweet = 1
	  else:
	    text = tweet.full_text
	    created_at = tweet.created_at 
	    favs = tweet.favorite_count
	    retweets = tweet.retweet_count

	    if tweet.entities['hashtags']:
		    hashtags = tweet.entities['hashtags'][0]['text']
	    else:
	        hashtags = ""

	    if tweet.entities['urls']:
	    	url = tweet.entities['urls'][0]['expanded_url']
	    else:
	    	url = ""

	    is_retweet = 0

	  nfkd_form = unicodedata.normalize('NFKD', text)
	  clean_text = nfkd_form.encode('ASCII', 'ignore') 
	  tweet_data = [ str(hashtags.encode('utf-8')),str(url.encode('utf-8')), str(created_at), str(favs), str(retweets), str(is_retweet)]
	  tweets.append(tweet_data)
	  tweet_text.append(str(clean_text))
	print("+ User has {} tweets.".format(len(tweets)))  
	return tweet_text,tweets



def get_following(user_id, api):
	# return account following by id
	ids = []
	sleeptime = 5
	pages = tweepy.Cursor(api.friends_ids, user_id=user_id, timeout=600).pages()

	while True:
	    try:
	        page = next(pages)
	        for tweet in page:
	        	ids.append(tweet)
	        time.sleep(sleeptime)

	    except tweepy.TweepError as e: #taking extra care of the "rate limit exceeded"
	        print(e.api_code)
	        time.sleep(60) 
	        try:
	        	page = next(pages)
	        except tweepy.TweepError as e:
	            print(e.api_code)
	            print("failed, user probably has protected account")
	            print(user_id)
	            return ids

	    except StopIteration:
	        break
		
	    if(len(ids) >= 10000):
		    print("user has {} followee".format(len(ids)))
		    return ids	

	print("user has {} following".format(len(ids)))
	
	return ids
	
"""
def get_bot_following(user_id, api, bom):



def get_geo(user_id, api):
"""
