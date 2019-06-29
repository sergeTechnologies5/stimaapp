# main.py

import requests 
from app.models import Stima 
from flask import (Blueprint,redirect, render_template,session, url_for)
main = Blueprint('main', __name__)

@main.route('/')
def index():
    session['logged_in'] = False
    return render_template("index.html", session=session.get('logged_in'))

@main.route('/profile',  methods=["GET", "POST"] )
def profile():
    stima = Stima.query.all()
    if stima :
        value = str(obj[-1].id)
    value = 0000.0
    return render_template('dashboard.html',value = value)


@main.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")

@main.route('/on',  methods=["GET", "POST"] )
def on():
    print("on")
    # api-endpoint 
    URL = "http://192.168.0.195:8081/?bulbAll=0"

    # sending get request and saving the response as response object 
    r = requests.get(url = URL) 
    return redirect(url_for('main.profile'))

@main.route('/off',  methods=["GET", "POST"] )
def off():
    # api-endpoint 
    URL = "http://192.168.0.195:8081/?bulbAll=1"
    
    # sending get request and saving the response as response object 
    r = requests.get(url = URL) 
    print("off")
    return redirect(url_for('main.profile'))