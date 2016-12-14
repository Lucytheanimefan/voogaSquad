import datetime
import JSONEncoder
from JSONEncoder import *
import ast

timestamp = None

def todaysdate():
	print "--------------todaysdate called-----------------"
	timestamp = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
	return timestamp

def getAllGameTimes(maincollection):
	gametimes = maincollection.find({ "type": "timerecord" })
	print "Game times: "
	games = [JSONEncoder().encode(game) for game in gametimes]
	return games

def record_actual_score(maincollection, score):
	timestamp = todaysdate()
	if (maincollection.find({"type": "myscore"}).count() == 0):
		print "CREATE score RECORD"
		scorerecord = {}
		scorerecord["type"]="myscore"
		scorerecord["data"]=[[timestamp, score]]
		maincollection.insert(scorerecord)
	else:
		maincollection.update({'type':"myscore"}, 
		{'$push': {"data": [timestamp, score]}})

def get_actual_score(maincollection):
	stats = {}
	scores = maincollection.find({ "type": "myscore" })
	newscores = [JSONEncoder().encode(score) for score in scores]
	print newscores
	return newscores

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


def log_end_score(maincollection, data):
	dat = {}
	data["timestamp"] = todaysdate()
	if (maincollection.find({"type": "endscore"}).count() == 0):
		print "CREATE ENDSCORE RECORD"
		dat["type"] = "endscore"
		dat["data"] = [data]
		maincollection.insert(dat)
	else:
		maincollection.update({'type':"endscore"}, 
		{'$push': {"data": data}})

	

def update_score(maincollection, level, updated_field, num):
	global timestamp
	maincollection.update({'gametime':timestamp}, 
		{'$push': {updated_field: [num,timestamp]}})
		

def get_game_for_time(maincollection, game_time):
	print "in stats get game for time"
	print "game time used to search"
	#print game_time
	games = maincollection.find({ "gametime": str(game_time)})
	#print games
	print "TYPE"
	data= [JSONEncoder().encode(game) for game in games][0]
	return data

def get_stats(maincollection):
	stats = {}
	scores = maincollection.find({ "type": "gamescore" })
	newscores = [JSONEncoder().encode(score) for score in scores]
	print newscores
	return newscores

def remove_stats(maincollection):
	print maincollection
	maincollection.remove({"type":"gamescore"})
	maincollection.delete_many({})


def get_end_scores(maincollection):
	top_scores = {}
	scores = maincollection.find({"type":"endscore"})
	data= [JSONEncoder().encode(score) for score in scores]
	print data
	return data

def get_num_games_played(maincollection):
	return maincollection.find({"type":"gamescore"}).count()


