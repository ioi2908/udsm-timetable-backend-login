from flask import Flask
#from flask_cors import CORS
import os



app = Flask(__name__)
#CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))

from app.view import *