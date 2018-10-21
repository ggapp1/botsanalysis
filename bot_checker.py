# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import tweepy
import botometer
import data
import pandas as pd
import os

consumer_key = 'GzDn8QwV3mIdnStJFMyyl2B5P'
consumer_secret= 'mwWVpg8wsYwU6SvLehCUJTTuBzDrspeqATghFm6fFXCQmOoklk'
access_token = '513768992-EGca4a9hTSBWigfMBdUFd31n793XufuDqVLlT90O'
access_token_secret= 'SjKQhu3VnTB2YawRrb7biKJXxwAbygZH2ETqu7YG2N3Zo'

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

files = [ 
		"#BolsonaroNao_bots" ]

for f in files:
	print("### CHECKING "+f)
	i = 0
	t = 0
	bots_file = open("checked_"+f, "w+")
	bots_file.write("user_id score\n")
	bots_file.flush()
	os.fsync(bots_file.fileno())

	uf = pd.read_csv(f, skiprows=1, names = ['user_id','score'])
	user_list = uf['user_id'].tolist()

	for user_id in user_list:
		user_score = 0
		user_score = data.bot_score(user_id, bom)
		t = t + 1
		print(t)
		if(user_score > 0.7):
			print("Probably bot. id " + str(user_id))
			print ("score "  + str(user_score))

			bots_file.write("{},{}\n".format(user_id, user_score))
			bots_file.flush()
			os.fsync(bots_file.fileno())
			i = i + 1

		if(i > 20):
			bots_file.write("{},{}\n".format(i, t))
			break;	

	print("bots founded: "+ str(i))
	bots_file.close()		 