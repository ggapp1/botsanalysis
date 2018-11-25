# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import tweepy
import time
import botometer
import data
import unicodedata
import os.path


api = data.generate_API()

bom = data.generate_Botometer()

def main():
  init = open('visited').read().splitlines()
  users = [int(i) for i in init]
  print(len(users))
  wrapped = 0
  sleeptime = 10
  for user_id in users:
  	if os.path.exists("files/tweets/tweets_"+str(user_id)):
  		print("! already collected")
  	else:
	    user_file = open("files/tweets/tweets_"+str(user_id), "w+")
	    print("getting user info")
	    try:
	    	user_score = data.bot_score(user_id, bom)
	    except:
	    	time.sleep(sleeptime*6) 
	    	user_score = data.bot_score(user_id, bom)	
	    print("now user info")
	    try:
		    user_obj = api.get_user(user_id)
		    time.sleep(sleeptime)
	    except tweepy.TweepError as e:
	    	print(e.api_code)
	    	time.sleep(sleeptime*10) 
	    	try:    
		     	print(e.api_code)
		     	time.sleep(sleeptime*10)			
		     	user_obj = api.get_user(user_id)
	    	except tweepy.TweepError as e:
		        print(e.api_code)
		        print("failed")
		        print(user_id)
		        break

	    user_file.write("{},{}\n".format(user_id, user_score))
	    user_file.write("{},{},{}\n".format(user_obj.followers_count, user_obj.friends_count, user_obj.statuses_count))
	    user_file.write("{}\n".format(user_obj.created_at))

	    tweets, datas = data.get_tweets(user_id, api)
	    for  tweet_data, tweet in zip(datas, tweets):
	     	user_file.write("{}\n".format(tweet))
	     	user_file.write(','.join(tweet_data)+"\n")

	    user_file.close()
	    wrapped = wrapped + 1
	    print("# got user. Count: "+str(wrapped))

if __name__ == '__main__':
  main()
  
