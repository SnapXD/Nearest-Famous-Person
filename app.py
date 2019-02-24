##############################################
# Project Header
#
# CrimsonCode Hackaton 2019 - 2/23/2019
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
# from flask import Response
# from flask_login import LoginManager, UserMixin, current_user, login_user, login_required
# from getpass import getpass
# from flask import current_app
from TwitterSearch import *
# import datetime


# app = Flask(__name__)
# login_manager = LoginManager()
# login_manager.init_app(app)
# CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlalchemy-demo.db'
#
# db = sqlalchemy.SQLAlchemy(app)
#
# base_url = 'https://api.twitter.com/1.1/search/tweets.json'

if __name__ == "__main__":
    try:
        tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
        tso.set_geocode(46.7281109, -117.1656875, 15, False)  # search tweets within 15 miles of the spark

        ts = TwitterSearch(
            consumer_key='placeholder',
            consumer_secret='placeholder',
            access_token='placeholder',
            access_token_secret='placeholder'
        )

        for tweet in ts.search_tweets_iterable(tso):
            print(tweet)

    except TwitterSearchException as e:
        print(e)
