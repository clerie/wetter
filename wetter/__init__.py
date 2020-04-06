#!/usr/bin/env python3

from wetter.config.db import db as config_db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = config_db['uri']

db = SQLAlchemy(app)

from wetter.models import *

import wetter.views
