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

hashtags = ["#DebateNaBand_bots",	  "#EleNao_bots","#VemProDebate_bots" ,
	    "#DebateNaGlobo_bots" ,"#EleSim_bots"	,  "#ViraViraCIR0_bots",
    "#DebateNaRecord_bots" ,"#ForaPT_bots","#DebateSBT_bots" ,
    "#HaddadÉLula_bots", "#Eleições2018_bots",	"#HaddadSim_bots"]

for hashtag in hashtags:
  data.get_bots_by_hashtag(hashtag, api, bom)


