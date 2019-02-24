##############################################
# Project Header
#
# CrimsonCode Hackathon 2019 - 2/23/2019
# Programmers:
#  Christopher Roberts
#  Brandon Garza
#  Sean Luchessa
#  Jesus Cruz
#
# File Header
#
# Name: app.py
# Path: Nearest-Famous-Person/static/app.py
# Description:
#  This file handles the backend for our website.  We will have the route handlers
#  and possibly a database to store recent searches.  This file will take a route call
#  from the JS file and sends the required request to Twitter, and possibly other
#  social media websites.  We will be returned a massive json object with many results.
#  This file will then filter out the unwanted data, then sort remaining by popularity
#  and return the most popular person to the JS.
#
##############################################

from flask import Flask, jsonify, request
from flask_cors import CORS
import flask_sqlalchemy as sqlalchemy
from flask import redirect, url_for
from flask import Flask, jsonify, request
from flask_cors import CORS
import flask_sqlalchemy as sqlalchemy
from flask import redirect, url_for
from TwitterSearch import *
# import datetime


app = Flask(__name__)
# login_manager = LoginManager()
# login_manager.init_app(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlalchemy-demo.db'
#
db = sqlalchemy.SQLAlchemy(app)
#
base_url = '/api/'


# this should redirect to the home page
@app.route('/')
def begin():
    print("webpage")
    return redirect(url_for(filename="UserInterface.html"))


@app.route(base_url + "get_tweets", methods=["GET"])
def get_tweets(location):
    try:
        tso = TwitterSearchOrder()  # create a TwitterSearchOrder object

        # search tweets within 15 miles of the spark. this will be changed to the geocode of the location parameter
        tso.set_geocode(46.7281109, -117.1656875, 15, False)

        ts = TwitterSearch(
            consumer_key='placeholder',
            consumer_secret='placeholder',
            access_token='placeholder',
            access_token_secret='placeholder'
        )

        for tweet in ts.search_tweets_iterable(tso):  # should filter out unverified users here
            print(tweet)  # we should add all of these into a dictionary or a list and return the closest one

        # find the closest tweet from the dictionary / list and return tweet['user']. (This is a string)

    except TwitterSearchException as e:
        print(e)
