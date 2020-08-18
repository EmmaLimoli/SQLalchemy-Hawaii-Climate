#flask jsonify to convert API data into json response object
#dependencies 
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_

from flask import Flask, jsonify

#database setup
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

#reflect an existing database into new model
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect=True)

#save references to the table
Measurement = Base.classes.measurement

Station = Base.classes.station

#Flask setup
app = Flask(__name__)

#Flask Routes
@app.route("/")
def welcome():
    """All available api routes."""
    return(
        f"Available Routes:<br/>"
        f"List of percipitation per date: /api/v1.0/precipitation<br/>"
        f"List of available stations: /api/v1.0/stations<br/>"
        f"List of temperature observations per date: /api/v1.0/tobs<br/>"
        f"List of max, min, and avg temperatures for a start date: /api/v1.0/yyyy-mm-dd<br/>"
        f"List of max, min, and avg temperatures for a start and end date: /api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/>"
    )
#precipitation, convert query results to a dict using date as the key and prcp as value
#use session, remember to close before for loop
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Previous year of precipitation"""
    session = Session(engine)
    date_prcp = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > '2016-08-22').\
    filter(Measurement.prcp).\
    order_by(Measurement.date).all()
    session.close()

    all_prcp = []
    for date, prcp in date_prcp:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_prcp.append(prcp_dict)
    return jsonify(all_prcp)

#stations, return jsonify list of stations from dataset
#use session, remember to close before for loop
@app.route("/api/v1.0/stations")
def stations():
    """List of stations"""
    session = Session(engine)
   
    stations = {}
    all_stations = session.query(Station.station, Station.name).all() 
    session.close()
    
    for st, name in all_stations:
       stations[st] = name
    return jsonify(stations)

#tobs, query dates/tobs of most active station for last year of data
#use session, remember to close before for loop
@app.route("/api/v1.0/tobs")
def tobs():
    """Previous year of temperature observations for top station"""
    session = Session(engine)
    last_12_months_station = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date > '2016-08-22').\
    order_by(Measurement.station).all()
    session.close()

    all_tobs = []
    for date, tobs in last_12_months_station:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_tobs.append(tobs_dict)
    return jsonify(all_tobs)

#return JSON list of min, avg, max temp for given start
#given start calc TMIN, TAVG, TMAX for dates greater than/equal to start date
#use session, remember to close before for loop
@app.route("/api/v1.0/<start>")
def start(start):
    """TMIN, TAVG, TMAX per date from the starting date.
    Arguments: start (string): date format is %Y-%m-%d
    Return: TMIN, TAVE, TMAX for each date"""

    session = Session(engine)
    tobs_breakdown = session.query(Measurement.date,\
    func.min(Measurement.tobs),\
    func.avg(Measurement.tobs),\
    func.max(Measurement.tobs)).\
    filter(Measurement.date >= '2010-01-01').\
    group_by(Measurement.date).all()
    session.close()

    tobs_results = []
    for date, min, avg, max in tobs_breakdown:
        results_dict = {}
        results_dict["date"] = date
        results_dict["min"] = min
        results_dict["avg"] = avg
        results_dict["max"] = max
        tobs_results.append(results_dict)
    return jsonify(tobs_results)


#given start/end date, calc TMIN, TAVG, TMAX for dates between start and end dates
#dates greater than and equal to the start date
#use session, remember to close before for loop
@app.route("/api/v1.0/<start>/<end>")
def end(start, end):
    """TMIN, TAVG, TMAX per date from the starting date to the end date.
    Arguments: 
            start (string): date format is %Y-%m-%d
            end (string): date format is %Y-%m-%d
    Return: TMIN, TAVE, TMAX for each date"""

    session = Session(engine)
    tobs_breakdown = session.query(Measurement.date,\
    func.min(Measurement.tobs),\
    func.avg(Measurement.tobs),\
    func.max(Measurement.tobs).\
    filter(Measurement.date >= '2010-01-01', Measurement.date <= end)).\
    group_by(Measurement.date).all()
    session.close()

    tobs_end = []
    for date, min, avg, max in tobs_breakdown:
        end_dict = {}
        end_dict["date"] = date
        end_dict["min"] = min
        end_dict["avg"] = avg
        end_dict["max"] = max
        tobs_end.append(end_dict)
    return jsonify(tobs_end)

#app.run debug to run 
if __name__=='__main__':
    app.run(debug=True)
