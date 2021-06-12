import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()
# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)
# Print all of the classes mapped to the Base
Base.classes.keys()
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>""<br/>"
        f"Return a list of precipitation and date, in JSON representation of dictionary<br/>"
        f"/api/v1.0/precipitation<br/>""<br/>"
        f"Return a JSON list of stations<br/>"  
        f"/api/v1.0/stations<br/>""<br/>" 
        f"Return a JSON list the dates and temperature observations of the **most active station** for the most recent 12 months of data""<br/>"
        f"/api/v1.0/tobs<br/>""<br/>"
        f"Return a JSONified dictionary of the min, max, and avg for all dates greater than and equal to the start date (YYYY-MM-DD)""<br/>"
        f"/api/v1.0/2017-08-23<br>""<br/>"
        f"Return a JSONified dictionary of the min, max, and avg for dates between the start and end date inclusive (YYYY-MM-DD)""<br/>"
        f"/api/v1.0/2017-08-22/2017-08-23<br/>"

    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation and date"""
    # Find the most recent date in the data set.
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first() 
    
    # date 365 days ago from today
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    result = session.query(Measurement.date, func.avg(Measurement.prcp)).group_by(Measurement.date).\
    order_by(Measurement.date).filter(Measurement.date >= year_ago).all()
    
    session.close()

        # Create a dictionary from the row data and append to a list of all_passengers
    # prcp_rows = [{"Date": result[0], "Precipitation": result[1]} for result in result]

    return jsonify(dict(result))

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations"""
    # List the station and name
    result = session.query(Station.station, Station.name).all()

    session.close()

    return jsonify(list(result))

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the dates and temperature observations of the **most active station** for the most recent 12 months of data"""
    # Find the most recent date in the data set.
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first() 
    
    # date 365 days ago from today
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # query the most active station in the last 12 months
    active = session.query(Measurement.station).\
    group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).\
    filter(Measurement.date >= year_ago).first()

    # query tobs for the most active station
    result = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == active[0]).all()

    session.close()

    return jsonify(lsit(result))

@app.route("/api/v1.0/<start>")
def startdate(start):
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """Return the min, max, and avg for all dates greater than and equal to the start date """
    results = session.query(func.max(Measurement.tobs), func.min(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter(Measurement.date >= start).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    dict_tobs = [{"Max": result[0], "Min": result[1], "Avg": result[2] } for result in results]
    
    
    return jsonify(dict_tobs)

@app.route("/api/v1.0/<start>/<end>")
def startend(start,end):
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the min, max, and avg for dates between the start and end date inclusive. """
    results = session.query(func.max(Measurement.tobs), func.min(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    dict_tobs = [{"Max": result[0], "Min": result[1], "Avg": result[2] } for result in results]
    
    return jsonify(dict_tobs)

if __name__ == '__main__':
    app.run(debug=True)
