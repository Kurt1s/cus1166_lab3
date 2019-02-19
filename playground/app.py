import sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import *
from config import Config
from flask_migrate import Migrate

c1 = ('Software Engineering', 1166)
c2 = ('Art History', 1050)
c3 = ('Psychology', 1177)
c4 = ('Biology', 1000)
c5 = ('Statistics I', 1077)
courses = [c1,c2,c3,c4,c5]

app = Flask(__name__)
app.debug = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)

app.config.from_object(Config)

db.create_all()

@app.route("/")
def index():
    return render_template("index.html", courses = courses)
    # return render_template("index.html")

# @app.route("/add_course")
# def index():
#     return render_template("index.html")
    
if __name__ == "__main__":
    with app.app_context():
        app.run(debug = True)