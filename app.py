import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///happiness_alcohol.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
happy = Base.classes.HappinessAlcoholConsumption

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# @app.route("/")
# def welcome():
#     """List all available api routes."""
#     return (
#         f"Available Routes:<br/>"
#         f"/api/v1.0/names<br/>"
#         f"/api/v1.0/passengers"
#     )


# @app.route("/api/v1.0/names")
# def names():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(Passenger.name).all()

#     session.close()

#     # Convert list of tuples into normal list
#     all_names = list(np.ravel(results))

#     return jsonify(all_names)


@app.route("/")
def happiness():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(happy.Country, happy.Region, happy.Hemisphere, happy.HappinessScore, happy.HDI, happy.GDP_PerCapita, happy.Beer_PerCapita, happy.Spirit_PerCapita, happy.Wine_PerCapita).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_countries = []
    for Country, Region, Hemisphere, HappinessScore, HDI, GDP_PerCapita, Beer_PerCapita, Spirit_PerCapita, Wine_PerCapita in results:
        country_dict = {}
        country_dict["Country"] = Country,
        country_dict["Region"] = Region,
        country_dict["Hemisphere"] = Hemisphere,
        country_dict["HappinessScore"] = HappinessScore,
        country_dict["HDI"] = HDI,
        country_dict["GDP_PerCapita"] = GDP_PerCapita,
        country_dict["Beer_PerCapita"] = Beer_PerCapita,
        country_dict["Spirit_PerCapita"] = Spirit_PerCapita,
        country_dict["Wine_PerCapita"] = Wine_PerCapita,
        all_countries.append(country_dict)

    return jsonify(all_countries)


if __name__ == '__main__':
    app.run(debug=True)
