import time
import datetime


def record_game_score(maincollection, goldlivesleveljson):
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	data = goldlivesleveljson
	data["time"]=st
	data["type"]="gamescore"
	maincollection.insert(data)

