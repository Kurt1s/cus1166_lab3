import sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import *
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.debug = True
db = SQLAlchemy(app)
migrate = Migrate(app, db) # this
db.init_app(app)

app.config.from_object(Config)

@app.route("/")
def index():
    courses = Course.query.all()
    render_template("index.html", courses = courses)

if __name__ == "__main__":
    with app.app_context():
        app.run(debug = True)