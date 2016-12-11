import datetime
import JSONEncoder
from JSONEncoder import *


timestamp = None

def todaysdate():
	timestamp = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
	return timestamp

def record_game_score(maincollection, goldlivesleveljson):
	global timestamp
	print "IN RECORD_GAME_SCORE"
	print goldlivesleveljson
	timestamp = todaysdate()
	dat = goldlivesleveljson
	dat["gametime"]=timestamp
	dat["type"]="gamescore"
	dat["gold"] = [[dat["gold"], timestamp]]
	dat["level"] =[[dat["level"][0], timestamp]]
	dat["lives"] = [[dat["lives"][0], timestamp]]
	maincollection.insert(dat)
	if (maincollection.find({"type": "timerecord"}).count() == 0):
		print "CREATE timee RECORD"
		timerecord = {}
		timerecord["type"]="timerecord"
		timerecord["time"]=[timestamp]
		maincollection.insert(timerecord)
	else:
		maincollection.update({'type':"timerecord"}, 
		{'$push': {"time": timestamp}})

	

def update_score(maincollection, level, updated_field, num):
	global timestamp
	print "-----------------------------------------------"
	print "update score with: level "
	print level
	print "updated field: "
	print updated_field
	print "field value: "
	print num
	print maincollection
	maincollection.update({'gametime':timestamp}, 
		{'$push': {updated_field: [num,timestamp]}})
		

def get_stats(maincollection):
	stats = {}
	scores = maincollection.find({ "type": "gamescore" })
	newscores = [JSONEncoder().encode(score) for score in scores]
	print newscores
	return newscores

