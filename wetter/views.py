#!/usr/bin/env python3

from wetter import app, excel
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

def export_target_ce(request, dwd_id):
    fr = fromisoformat(request.args.get('from'))
    to = fromisoformat(request.args.get('to'))

    station = Stations.query.filter_by(dwd_id=dwd_id).first_or_404()
    climate = Climate.query.filter_by(station=station.id).filter(Climate.date >= fr.isoformat(), Climate.date <= to.isoformat()).order_by(Climate.date.asc())

    out = [
        ["Datum", "Temperatur in °C"],
        [None, "Niederschlagsmenge in mm"],
        [None, "Windgeschwindigkeit in m/s"],
        [None, "Sonnenscheindauer in h"],
    ]

    for c in climate:
        out.append([c.date.isoformat(), str(c.tmk) + " °C"])
        out.append([None, str(c.rsk) + " mm"])
        out.append([None, str(c.fm) + " m/s"])
        out.append([None, str(c.sdk) + " h"])

    filename = 'wetter_' + station.dwd_id +'_' + fr.isoformat() + '_' + to.isoformat() +'_ce'

    return out, filename

@app.route('/station/<dwd_id>/export/target/ce.csv/')
def export_target_ce_csv_render(dwd_id):
    out, filename = export_target_ce(request, dwd_id)

    return excel.make_response_from_array(out, 'csv', file_name=filename)

@app.route('/station/<dwd_id>/export/target/ce.xlsx/')
def export_target_ce_xlsx_render(dwd_id):
    out, filename = export_target_ce(request, dwd_id)

    return excel.make_response_from_array(out, 'xlsx', file_name=filename)

def export_target_dwd(request, dwd_id):
    fr = fromisoformat(request.args.get('from'))
    to = fromisoformat(request.args.get('to'))

    station = Stations.query.filter_by(dwd_id=dwd_id).first_or_404()
    climate = Climate.query.filter_by(station=station.id).filter(Climate.date >= fr.isoformat(), Climate.date <= to.isoformat()).order_by(Climate.date.asc())

    out = []
    out.append(["STATIONS_ID", "MESS_DATUM", "QN_3",  "FX",  "FM", "QN_4", "RSK", "RSKF", "SDK", "SHK_TAG", "NM", "VPM",  "PM", "TMK", "UPM", "TXK", "TNK", "TGK", "eor"])

    for c in climate:
        out.append([ station.dwd_id, c.date.isoformat(), c.qn_3, c.fx, c.fm, c.qn_4, c.rsk, c.rskf, c.sdk, c.shk_tag, c.nm, c.vpm, c.pm, c.tmk, c.upm, c.txk, c.tnk, c.tgk, "eor"])

    filename = 'wetter_' + station.dwd_id +'_' + fr.isoformat() + '_' + to.isoformat() +'_dwd'

    return out, filename

@app.route('/station/<dwd_id>/export/target/dwd.csv/')
def export_target_dwd_csv_render(dwd_id):
    out, filename = export_target_dwd(request, dwd_id)

    return excel.make_response_from_array(out, 'csv', file_name=filename)

@app.route('/station/<dwd_id>/export/target/dwd.xlsx/')
def export_target_dwd_xlsx_render(dwd_id):
    out, filename = export_target_dwd(request, dwd_id)

    return excel.make_response_from_array(out, 'xlsx', file_name=filename)

@app.route('/station/<dwd_id>/export/target/dwd.txt/')
def export_target_dwd_txt_render(dwd_id):
    fr = fromisoformat(request.args.get('from'))
    to = fromisoformat(request.args.get('to'))

    station = Stations.query.filter_by(dwd_id=dwd_id).first_or_404()
    climate = Climate.query.filter_by(station=station.id).filter(Climate.date >= fr.isoformat(), Climate.date <= to.isoformat()).order_by(Climate.date.asc())

    r = make_response(render_template('export/dwd.txt', station=station, climate=climate))
    r.headers['Content-Type'] = 'text/txt; charset=utf-8'
    r.headers['Content-Disposition'] = 'attachment; filename="wetter_' + station.dwd_id +'_' + fr.isoformat() + '_' + to.isoformat() +'_dwd.txt"'

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
