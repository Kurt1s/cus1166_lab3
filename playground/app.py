import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import *
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.debug = True
db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)

# db.create_all()

c1 = ('Software Engineering', 1166)
c2 = ('Art History', 1050)
c3 = ('Psychology', 1177)
c4 = ('Biology', 1000)
c5 = ('Statistics I', 1077)
courses = [c1,c2,c3,c4,c5]

@app.route("/")
def index():
    return render_template("index.html", courses = courses)
    # return render_template("index.html")

@app.route("/add_course", methods = ["post"])
def add_flight():
    course_id = request.form.get("course_id")
    course_number = request.form.get("course_number")
    course_title = request.form.get("course_title")
    course = Course(course_id = course_id, course_number=course_number, course_title=course_title)

    db.session.add(flight)
    db.session.commit()
    courses = Course.query.all()
    return render_template('add_flight.html', courses = courses, form=form)


if __name__ == "__main__":
    with app.app_context():
        app.run(debug = True)