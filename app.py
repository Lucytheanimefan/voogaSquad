import os
from flask import Flask
from flask import render_template,jsonify,request, redirect,url_for
import csv
import sys
import server
from server import *
import sys
import json
from JSONEncoder import JSONEncoder
from login import *
import json, xmltodict
import stats
from stats import *

app = Flask(__name__)

db = server.get_db()

username = ""
mygames={}

maincollection = None


reload(sys)
sys.setdefaultencoding('utf-8')


def set_username(new_username):
	global username
	username = new_username

def set_maincollection(collection):
	global maincollection
	maincollection = collection

def set_games():
	print "setting games"
	global mygames
	global username
	print "Username! "+username
	mygames = {}
	if (db[username].count() > 0):
		if (db[username].find({ "type": "game" }).count()>0):
			games = db[username].find({ "type": "game" });
			i = 0
			for game in games:
				mygames["Game "+str(i)] = JSONEncoder().encode(game)
				i = i+1
			print "MY GAMES"
			print mygames


@app.route("/")
def home():
	return render_template('login.html')


@app.route("/home")
def main():
	if username=="":
		return home()
	global mygames
	set_games()
	print "render main template"
	return render_template('index3.html', username=username, games = mygames)


@app.route("/game")
def game():
	if username=="":
		return home()
	global mygames
	set_games()
	return render_template('games.html', username=username, games=mygames)

@app.route("/login",methods=['POST','GET'])
def login():
	if username=="":
		open_account(request.json['username'], request.json['password'])
		set_username(request.json['username'])
		set_maincollection(db[username])
		set_games()
	else:
		return "already logged in" 
	return "logged in"
	#return render_template('index3.html', games = mygames)

@app.route("/logout",methods=['POST','GET'])
def logout():
	print "logging out"
	set_username("")
	set_maincollection(None)
	return "Logged out"


@app.route("/createaccount",methods=['POST','GET'])
def createaccount():
	print "creating account with: " + request.json['username']+" "+request.json['password']
	create_account(request.json['username'], request.json['password'])
	return "created account"

@app.route("/creategame",methods=['POST','GET'])
def create_games():
	print "CREATING GAMES"
	print request.get_json()
	gamejson = request.get_json()
	#print gamejson
	maincollection.insert(gamejson)
	return "Successfully created game in creategame"

@app.route("/recordscore",methods = ['POST','GET'])
def record_score():
	print "In record_score"
	print request.get_json()
	record_game_score(maincollection, request.get_json())
	return "Successfully recorded score"

@app.route("/updatescore",methods = ['POST','GET'])
def updatescore():
	print 'UPDATE_ SCORE JSON:'
	print request.get_json()
	update_score(maincollection, request.json['level'], request.json['updated_field'], request.json['value'])
	return "Successfully Updated Score"

@app.route("/getgamescores", methods = ['GET'])
def getgamescores():
	data = get_stats(maincollection)
	return jsonify(result = data)


@app.route("/getgametimes", methods = ['GET'])
def getgametimes():
	data = getAllGameTimes(maincollection)
	return jsonify(result = data)


@app.route("/remove", methods=['GET'])
def remove():
	remove_stats(maincollection)
	return "success remove"


@app.route("/get_game_for_time", methods=['GET','POST'])
def getgamefortime():
	print "In get game for time"
	game_time = request.json['game_time']
	print game_time
	return get_game_for_time(maincollection, game_time)

@app.route("/logScore", methods=['GET','POST'])
def logScore():
	record_actual_score(maincollection, request.json['score'])
	return "Logged score"

@app.route("/log_end_score",methods=['GET','POST'])
def logendscore():
	data = request.get_json()
	log_end_score(maincollection, data)
	return "Logged end score of game"

@app.route("/get_actual_score", methods = ['GET'])
def getActualScore():
	return jsonify(result=get_actual_score(maincollection))

@app.route("/get_end_scores",methods=['GET'])
def getendscore():
	data = get_end_scores(maincollection)
	return jsonify(result=data) 

@app.route("/num_games",methods=['GET'])
def getnumgames():
	return str(get_num_games_played(maincollection))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)