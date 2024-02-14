# Python standard libraries
import json
import os

# Third party libraries
from flask import Flask
from mongoengine import connect
from flask_login import LoginManager
#from oauthlib.oauth2 import WebApplicationClient
import certifi
from app.utils.secrets import getSecrets
from flask_moment import Moment
import base64

# Flask app setup
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or os.urandom(24)

# Configuration
secrets = getSecrets()

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Naive database setup
connect(secrets['MONGO_DB_NAME'], host=secrets['MONGO_HOST'], tlsCAFile=certifi.where())
moment = Moment(app)

def base64encode(img):
    image = base64.b64encode(img)
    image = image.decode('utf-8')
    return image

app.jinja_env.globals.update(base64encode=base64encode)

from .routes import *


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://TheLaw30:<password>@thelaw30.orcahbv.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)