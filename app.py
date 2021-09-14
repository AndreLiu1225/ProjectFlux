from flask import Flask, jsonify, request, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy, _EngineConnector
# import flask_whooshalchemy as wa
import sqlite3
from waitress import serve

# TODO: create database, import csv files into database, finish whoosh search.

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['WHOOSH_BASE'] = 'whoosh'

con = sqlite3.connect("site.db", check_same_thread=False)
cur = con.cursor()

db = SQLAlchemy(app)

# Database to store policies
class Policy(db.Model):
    __searchable__ = ['country_name']

    country_name = db.Column(db.String(50), primary_key=True)
    contact_trace = db.Column(db.Integer)
    inter_travel = db.Column(db.Integer)
    movement_res = db.Column(db.Integer)
    public_trans = db.Column(db.Integer)
    test_pol = db.Column(db.Integer)
    vaccine_pol = db.Column(db.Integer)

# wa.whoosh_index(app, Policy)

# Search policy form
class PolicySearchForm(Form):
    country = StringField("country", validators=[DataRequired()])
    submit = SubmitField("Search")
    
@app.route('/api')
def api():
    return render_template("api.html")

@app.route('/contactUs')
def contactUs():
    return render_template("contact_us.html")

@app.route("/team")
def team():
    return render_template("our_team.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=["GET", "POST"])
def search():
    form = PolicySearchForm()
    if request.method == "POST":
        country = request.form["country"]
        cur.execute("SELECT contact_trace, inter_travel, movement_res, public_trans, test_pol, vaccine_pol from policy WHERE country_name LIKE ?", (country,))
        con.commit()
        data = cur.fetchall()
        if len(data)==0 and country=="all":
            cur.execute("SELECT contact_trace, inter_travel, movement_res, public_trans, test_pol, vaccine_pol from policy")
            con.commit()
            data = cur.fetchall()
        return render_template("results.html", data=data)
    return render_template("home.html", form=form)

if __name__ == '__main__':
    app.run()
