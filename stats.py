import datetime


def record_game_score(maincollection, goldlivesleveljson):
	print "IN RECORD_GAME_SCORE"
	print goldlivesleveljson
	timestamp = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
	print timestamp 
	dat = goldlivesleveljson
	dat["time"]=timestamp
	dat["type"]="gamescore"
	maincollection.insert(data)

