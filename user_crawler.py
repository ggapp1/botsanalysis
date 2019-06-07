# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import tweepy
import time
import botometer
import data
import unicodedata

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


#get net of haddad and bolso
users = [354095556, 128372940]

# Check a single account followers by id


for user_id in users:
  followers = data.get_followers(user_id, api)
  flbots_file = open("flbots_"+user_id, "w+")
  flbots_file.write("user_id score\n")
  flbots_file.flush()
  os.fsync(flbots_file.fileno())
  i = 0
  t = 0
  for follower in followers:
    fl_score = data.bot_score(user_id, bom)
    t = t + 1
    
  flbots_file.write("{},{}\n".format(i, t))
  flbots_file.close()
"""
    if(fl_score > 0.7)
      flbots_file.write("{},{}\n".format(user_id, fl_score))
      i = i + 1 
      bots_file.flush()
      os.fsync(bots_file.fileno())

    if(i > 50):
      flbots_file.write("{},{}\n".format(i, t))
      flbots_file.close()
      break    
"""

