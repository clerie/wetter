#!/usr/bin/env python3

from wetter.config.db import db as config_db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_excel as excel

app = Flask(__name__)
excel.init_excel(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = config_db['uri']

db = SQLAlchemy(app)

from wetter.models import *

import wetter.views
