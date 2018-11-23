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

def main():
  init = open('visited').read().splitlines()
  users = [int(i) for i in init]
  print(len(users))
  wrapped = 0
  for user_id in users:
    user_file = open("files/tweets/tweets_"+str(user_id), "w+")
    user_score = data.bot_score(user_id, bom)
    user_obj = api.get_user(user_id)
    user_file.write("{},{}".format(user_id, user_score))
    user_file.write("{},{},{}\n".format(user_obj.followers_count, user_obj.friends_count, user_obj.statuses_count))
    user_file.write("{}\n".format(user_obj.created_at))

    tweets = data.get_tweets(user_id, api)

    for tweet in tweets:
      user_file.write(','.join(tweet)+"\n")

    user_file.close()
    wrapped = wrapped + 1
    print("# got user. Count: "+str(wrapped))

if __name__ == '__main__':
  main()
  
