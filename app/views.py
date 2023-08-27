from flask import render_template
from datetime import datetime
from __init__ import app
import statsapi
import pandas as pd
from operator import itemgetter

roster_json = statsapi.get('team_roster', {'teamId':142})

roster_table = pd.json_normalize(roster_json['roster'])
roster = []

for i in range(roster_table.shape[0]):
    roster.append([int(roster_table.at[i, 'jerseyNumber']), roster_table.at[i, 'person.fullName'], roster_table.at[i, 'position.abbreviation']])

roster.sort(key=itemgetter(0))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/twinsroster/")
def twinsroster():
    return render_template("twinsroster.html",roster=roster)