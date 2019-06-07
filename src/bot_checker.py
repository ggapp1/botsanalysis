# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import tweepy
import botometer
import data
import pandas as pd
import os

api = data.generate_API()
bom = data.generate_Botometer()

files = ["#BrasilComBolsonaro", "#bolsonaroCagao"  ,    "#bolsonaroSim " ,
"#DebateNaBand_bots",	  "#EleNao_bots","#VemProDebate_bots" ,
	    "#DebateNaGlobo_bots" ,"#EleSim_bots"	,  "#ViraViraCIR0_bots",
    "#DebateNaRecord_bots" ,"#ForaPT_bots","#DebateSBT_bots" ,
    "#HaddadÉLula_bots", "#Eleições2018_bots",	"#HaddadSim_bots"]

for f in files:
	print("### CHECKING "+f)
	i = 0
	t = 0
	bots_file = open("suffle/checked_"+f, "w+")
	bots_file.write("user_id score\n")
	bots_file.flush()
	os.fsync(bots_file.fileno())

	uf = pd.read_csv("suffle/suffle_"+f, skiprows=1, names = ['user_id','score'])
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

		if(i > 200):
			bots_file.write("{},{}\n".format(i, t))
			break;	

	print("bots founded: "+ str(i))
	bots_file.close()		 

