from flask_sqlalchemy import SQLAlchemy
from app import db
import os, csv, sys

# db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'app.db')

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key = True)
    course_number = db.Column(db.String, nullable = False)
    course_title = db.Column(db.String, nullable = False)

    def add_course(id,number,title):
        # Notice that we set the foreign key for the passenger class.
        new_course = Course(title=title, number = number, id=self.id )
        db.session.add(new_course)
        db.session.commit()

        
class RegisteredStudent(db.Model):
    __tablename__ = "registeredstudents"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.Integer, nullable = False)

