from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://heroku_stn0kqjg:o13nvclintda4d0lgbnppv7o3v@ds119608.mlab.com:19608/heroku_stn0kqjg')
    db = client.heroku_stn0kqjg
    return db

