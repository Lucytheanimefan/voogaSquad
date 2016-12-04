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

app = Flask(__name__)

db = server.get_db()

username = ""
games=[]

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
	global games
	numgames = db.games.count();
	for i in numgames:
		games.append("Game "+str(i))


@app.route("/")
@app.route("/login")
def home():
	return render_template('login.html')


@app.route("/home")
def main():
	games={"game1","game2","game3"}
	print "render main template"
	return render_template('index3.html', username=username, games = games)


@app.route("/game")
def game():
	set_games()
	return render_template('games.html', username=username, games=games)

@app.route("/login",methods=['POST','GET'])
def login():
	print "logging in with: " + request.json['username']+" "+request.json['password']
	open_account(request.json['username'], request.json['password'])
	set_username(request.json['username'])
	set_maincollection(db[username])
	print username
	print "redirect!"
	return render_template('index3.html')


@app.route("/createaccount",methods=['POST','GET'])
def createaccount():
	print "creating account!"
	if request.method == "POST":
		print "post request!"
	elif request.methond == "GET":
		print "GET request"
	print "creating account with: " + request.json['username']+" "+request.json['password']
	create_account(request.json['username'], request.json['password'])
	return main()

@app.route("/creategame",methods=['POST','GET'])
def create_games():
	print "CREATING GAMES"
	global db
	print request.get_json()
	gamejson = request.get_json()
	print gamejson
	maincollection.insert(gamejson)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)