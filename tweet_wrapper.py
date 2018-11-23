# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import tweepy
import time
import botometer
import data
import unicodedata

api = data.generate_API()

mashape_key = "RWoa8U8jiImshcKeqzezdmcSr6M7p1U1plajsnTa1CF4tlKGTh"

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **api)

def main():
  users = [114312114]
  for user in users:
    user_file = open("files/tweets_"+str(user), "w+")
    user_score = data.bot_score(user_id, bom)
    user_obj = api.get_user(user)

    user_file.write("{},{}\n".format(user_id, user_score))
    user_file.write("{},{},{}\n".format(user_obj.follower_count, user_obj.friends_count, user_obj.statuses_count))
    user_file.write("{}\n".format(user_obj.created_at))

    tweets = data.get_tweets(user, api)

    for tweet in tweets:
      user_file.write(','.join(tweet))

    user_file.close()


if __name__ == '__main__':
  main()
  
