# main.py

from app.models import Stima 
from flask import (Blueprint, render_template,session, url_for)
main = Blueprint('main', __name__)

@main.route('/')
def index():
    session['logged_in'] = False
    return render_template("index.html", session=session.get('logged_in'))

@main.route('/profile',  methods=["GET", "POST"] )
def profile():
    return render_template('dashboard.html')


@main.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")

