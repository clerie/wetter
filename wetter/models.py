#/usr/bin/env python3

from wetter import db

class Stations(db.Model):
    __tablename__ = 'stations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    lat = db.Column(db.Integer)
    lon = db.Column(db.Integer)
    dwd_id = db.Column(db.String)
    dwd_last_update = db.Column(db.TIMESTAMP)

class Climate(db.Model):
    __tablename__ = 'climate'
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.Integer)
    date = db.Column(db.Date)
    qn_3 = db.Column(db.Integer)
    fx = db.Column(db.Float)
    fm = db.Column(db.Float)
    qn_4 = db.Column(db.Integer)
    rsk = db.Column(db.Float)
    rskf = db.Column(db.Integer)
    sdk = db.Column(db.Float)
    shk_tag = db.Column(db.Float)
    nm = db.Column(db.Float)
    vpm = db.Column(db.Float)
    pm = db.Column(db.Float)
    tmk = db.Column(db.Float)
    upm = db.Column(db.Float)
    txk = db.Column(db.Float)
    tnk = db.Column(db.Float)
    tgk = db.Column(db.Float)
    dwd_last_update = db.Column(db.TIMESTAMP)
