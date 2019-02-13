import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def index(): 
    courses = Course.query.all()
    render_template("index.html", courses = courses)







if name == "main":
    with app.app_context():
        main()