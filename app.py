from flask import Flask, jsonify, request
from flask_cors import CORS
import flask_sqlalchemy as sqlalchemy
from flask import redirect, url_for
from flask import Response
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required
from getpass import getpass
from flask import current_app
import datetime


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlalchemy-demo.db'

db = sqlalchemy.SQLAlchemy(app)

