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


app = Flask(__name__)

db = server.get_db()

username = ""

reload(sys)
sys.setdefaultencoding('utf-8')

def set_username(new_username):
	global username
	username = new_username

@app.route("/")
@app.route("/login")
def home():
	return render_template('login.html')


@app.route("/home")
def main():
	print "render main template"
	return render_template('index3.html', username=username)

@app.route("/login",methods=['POST','GET'])
def login():
	print "logging in with: " + request.json['username']+" "+request.json['password']
	open_account(request.json['username'], request.json['password'])
	set_username(request.json['username'])
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


@app.route('/populate',methods=['POST','GET'])
def search():
	global db
	doc = db.scholarprofiles.find()
	print '-------------------CURSOR------------'
	data = [JSONEncoder().encode(prof) for prof in doc]
	return jsonify(result = data)

'''
@app.route('/populatedb')
def populate():
	global reader
	global db
	for row in reader:
		db.scholarprofiles.insert({
			'Email':row[1].decode('latin-1').encode('utf-8'),
			'Name':parseName(row[2].decode('latin-1').encode('utf-8')),
			'Phone':row[3].decode('latin-1').encode('utf-8'),
			'Unviersity':row[4].decode('latin-1').encode('utf-8'),
			'Graduation':row[5].decode('latin-1').encode('utf-8'),
			'Intended Major':row[6].decode('latin-1').encode('utf-8'),
			'Parsed Intended Major':splitMajorMinor(row[6].decode('latin-1').encode('utf-8')),
			'Declared Major':row[7].decode('latin-1').encode('utf-8'),
			'Relevant Coursework':parseToArray(row[8].decode('latin-1').encode('utf-8')),
			'Interested Areas of Tech':parseToArray(row[9].decode('latin-1').encode('utf-8')),
			'Interested Areas of Industry':parseToArray(row[10].decode('latin-1').encode('utf-8')),
			'Special Skills/Qualifications':row[11].decode('latin-1').encode('utf-8'),
			'Computer programming skillset':row[12].decode('latin-1').encode('utf-8'),
			'Why KAC':row[13].decode('latin-1').encode('utf-8'),
			'Interest in specific company/position':row[14].decode('latin-1').encode('utf-8'),
			'Location Preference':parseToArray(row[15].decode('latin-1').encode('utf-8')),
			'3 interesting things':row[16].decode('latin-1').encode('utf-8'),
			'Reference':row[17].decode('latin-1').encode('utf-8')
			})
'''


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)