import time
import datetime


def record_game_score(maincollection, goldlivesleveljson):
	print "IN RECORD_GAME_SCORE"
	print goldlivesleveljson
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	data = goldlivesleveljson
	data["time"]=st
	data["type"]="gamescore"
	maincollection.insert(data)

