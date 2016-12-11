import datetime
import JSONEncoder
from JSONEncoder import *
import ast

timestamp = None

def todaysdate():
	timestamp = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
	return timestamp

def getAllGameTimes(maincollection):
	gametimes = maincollection.find({ "type": "timerecord" })
	print "Game times: "
	games = [JSONEncoder().encode(game) for game in gametimes]
	return games

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
	maincollection.update({'gametime':timestamp}, 
		{'$push': {updated_field: [num,timestamp]}})
		

def search_game(maincollection, game_time):
	game = maincollection.find({ "gametime": game_time})
	print game
	return JSONEncoder().encode(game)

def get_stats(maincollection):
	stats = {}
	scores = maincollection.find({ "type": "gamescore" })
	newscores = [JSONEncoder().encode(score) for score in scores]
	print newscores
	return newscores

