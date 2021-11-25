from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
import os
import sqlite3 as sql

#init app and class
app = Flask(__name__)

#initiate memory cache of database
conn = sql.connect('data/databases/animal_crossing_inventory.db')

###########################################

#route for all items list
@app.route("/")
def home():
    return render_template("index.html")

#route for all items list
@app.route("/allItems", methods=["POST"])
def allItems():
    return render_template("allItems.html")

#route for my items list
@app.route("/myItems", methods=["POST"])
def myItems():
    return render_template("myItems.html")

#route for favorite items list
@app.route("/favorites", methods=["POST"])
def favorites():
    return render_template("favorites.html")

#############################################################
conn.close()
#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
