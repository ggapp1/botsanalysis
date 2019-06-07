# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import tweepy
import time
import botometer
import data
import unicodedata

api = data.generate_API()
bom = data.generate_Botometer()


#get net of haddad and bolso
users = [354095556, 128372940]

# Check a single account followers by id

for user_id in users:
  followers = data.get_followers(user_id, api)
  flbots_file = open("flbots_"+user_id, "w+")
  flbots_file.write("user_id score\n")
  flbots_file.flush()
  os.fsync(flbots_file.fileno())
  fl_score = 0
  for follower in followers:
    fl_score = data.bot_score(user_id, bom)
    
  flbots_file.write("{},{}\n".format(user_id, fl_score))
  flbots_file.close()

