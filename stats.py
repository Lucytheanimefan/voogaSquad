import datetime
import JSONEncoder
from JSONEncoder import *


def record_game_score(maincollection, goldlivesleveljson):
	print "IN RECORD_GAME_SCORE"
	print goldlivesleveljson
	timestamp = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
	print timestamp 
	dat = goldlivesleveljson
	dat["time"]=[timestamp]
	dat["type"]="gamescore"
	maincollection.insert(dat)


def update_score(maincollection, level, updated_field, num):
	print "-----------------------------------------------"
	print "update score with: level "+level+" and "
	print updated_field updated_field
	print num
	timestamp = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
	print maincollection
	maincollection.update({'level':level}, 
		{'$push': {updated_field: [num,timestamp]}})
		

def get_stats(maincollection):
	stats = {}
	scores = maincollection.find({ "type": "gamescore" })
	newscores = [JSONEncoder().encode(score) for score in scores]
	print newscores
	return newscores

