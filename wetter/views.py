#!/usr/bin/env python3

from wetter import app
from wetter.models import Stations, Climate
from wetter.utils import fromisoformat
from flask import request, make_response, render_template, jsonify
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/station/')
def stations():
    stations = Stations.query.order_by(Stations.dwd_id.asc()).all()

    return render_template('stations.html', stations=stations)

@app.route('/station/<dwd_id>/')
def station(dwd_id):
    station = Stations.query.filter_by(dwd_id=dwd_id).first_or_404()

    return render_template('station.html', station=station)

@app.route('/station/<dwd_id>/export/')
def export(dwd_id):
    station = Stations.query.filter_by(dwd_id=dwd_id).first_or_404()

    return render_template('export.html', station=station)

@app.route('/station/<dwd_id>/export/target/')
def export_target(dwd_id):
    fr = fromisoformat(request.args.get('from'))
    to = fromisoformat(request.args.get('to'))

    station = Stations.query.filter_by(dwd_id=dwd_id).first_or_404()

    return render_template('target.html', station=station, fr=fr.isoformat(), to=to.isoformat())

@app.route('/station/<dwd_id>/export/target/ce.csv/')
def export_target_ce_csv_render(dwd_id):
    fr = fromisoformat(request.args.get('from'))
    to = fromisoformat(request.args.get('to'))

    station = Stations.query.filter_by(dwd_id=dwd_id).first_or_404()
    climate = Climate.query.filter_by(station=station.id).filter(Climate.date >= fr.isoformat(), Climate.date <= to.isoformat()).order_by(Climate.date.asc())

    r = make_response(render_template('export/ce.csv', climate=climate))
    r.headers['Content-Type'] = 'text/csv; charset=utf-8'
    r.headers['Content-Disposition'] = 'attachment; filename="wetter_' +station.dwd_id +'_' + fr.isoformat() + '_' + to.isoformat() +'_ce.csv'

    return r

@app.route('/station/<dwd_id>/export/target/dwd.txt/')
def export_target_dwd_txt_render(dwd_id):
    fr = fromisoformat(request.args.get('from'))
    to = fromisoformat(request.args.get('to'))

    station = Stations.query.filter_by(dwd_id=dwd_id).first_or_404()
    climate = Climate.query.filter_by(station=station.id).filter(Climate.date >= fr.isoformat(), Climate.date <= to.isoformat()).order_by(Climate.date.asc())

    r = make_response(render_template('export/dwd.txt', station=station, climate=climate))
    r.headers['Content-Type'] = 'text/txt; charset=utf-8'
    r.headers['Content-Disposition'] = 'attachment; filename="wetter_' + station.dwd_id +'_' + fr.isoformat() + '_' + to.isoformat() +'_dwd.txt'

    return r

@app.route('/api/station/')
def api_station():
    s = request.args.get('s')

    if s:
        station = Stations.query.filter_by(dwd_id=s).first_or_404()
        stations = [station]
    else:
        stations = Stations.query.order_by(Stations.lon.asc()).order_by(Stations.lat.desc()).all()

    out = []
    for s in stations:
        out.append({
            "name": str(s.name),
            "lat": float(s.lat),
            "lon": float(s.lon),
            "dwd_id": str(s.dwd_id),
        })

    return jsonify(out)
