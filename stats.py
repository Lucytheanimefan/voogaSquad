import datetime
import JSONEncoder
from JSONEncoder import *


def todaysdate():
	timestamp = '{:%Y-%b-%d}'.format(datetime.datetime.now())
	return timestamp

def record_game_score(maincollection, goldlivesleveljson):
	print "IN RECORD_GAME_SCORE"
	print goldlivesleveljson
	timestamp = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
	print timestamp 
	dat = goldlivesleveljson
	dat["time"]=todaysdate()
	dat["type"]="gamescore"
	dat["gold"] = [[dat["gold"], timestamp]]
	dat["level"] =dat["level"][0]
	dat["lives"] = [[dat["lives"][0], timestamp]]
	maincollection.insert(dat)
	if (maincollection.find({"type": "timerecord"}).count() == 0):
		timerecord = {}
		timerecord["type"]="timerecord"
		timerecord["time"]=[todaysdate()]
		maincollection.insert(timerecord)
	else:
		maincollection.update({'type':"timerecord"}, 
		{'$push': {"time": todaysdate()}})

	

def update_score(maincollection, level, updated_field, num):
	print "-----------------------------------------------"
	print "update score with: level "
	print level
	print "updated field: "
	print updated_field
	print "field value: "
	print num
	timestamp = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
	print maincollection
	maincollection.update({'time':todaysdate()}, 
		{'$push': {updated_field: [num,timestamp]}})
		

def get_stats(maincollection):
	stats = {}
	scores = maincollection.find({ "type": "gamescore" })
	newscores = [JSONEncoder().encode(score) for score in scores]
	print newscores
	return newscores

