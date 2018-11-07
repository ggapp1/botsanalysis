import sys, random

files  = ["#DebateNaBand_bots",	  "#EleNao_bots","#VemProDebate_bots" ,
	    "#DebateNaGlobo_bots" ,"#EleSim_bots"	,  "#ViraViraCIR0_bots",
    "#DebateNaRecord_bots" ,"#ForaPT_bots","#DebateSBT_bots" ,
    "#HaddadÉLula_bots", "#Eleições2018_bots",	"#HaddadSim_bots"]

for f in files:
	with open('suffle/'+f,'r') as source:
	    data = [ (random.random(), line) for line in source ]
	data.sort()
	with open('suffle/suffle_'+f,'w') as target:
	    for _, line in data:
        	target.write(line)