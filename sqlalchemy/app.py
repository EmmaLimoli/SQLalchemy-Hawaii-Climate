#need to join the station/measurement tabels for some of the queries
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
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<end>/<end><br/>"
    )
#precipitation, convert query results to a dict using date as the key and prcp as value
@app.route("/api/v1.0/precipitation")
def precipitation():
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

#open a session.bind, run the same query, taking in the JN and putting it into python
#it will create a list of tuples, use the first query, 

    #return json rep of jsonify

#stations, return jsonify list of stations from dataset
@app.route("/api/v1.0/stations")
def stations():
#calling the entire dateset of the station, calling on the session open and close, process data send it to the web
# #tobs, query dates/tobs of most active station for last year of data
# @app.route("/api/v1.0/tobs")
# def tobs():

#     #return JSON list of tobs for prev year

# #return JSON list of min, avg, max temp for given start-end range
# #given start calc TMIN, TAVG, TMAX for dates greater than/equal to start date
# @app.route("/api/v1.0/<start>")
# def 

# #given start/end date, calc TMIN, TAVG, TMAX for dates between start and end dates
# @app.route("/api/v1.0/<start>/<end>")

#app.run debug to run 
if __name__=='__main__':
    app.run(debug=True)
