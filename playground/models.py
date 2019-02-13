from flask_sqlalchemy import SQLAlchemy
sb = SQLAlchemy()

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key = True)
    course_number = db.Column(db.String, nullable)
    course_title = db.Column(db.String, nullable)

class RegisteredStudent():

    __tablename__ = "registeredstudents"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.Integer, nullable = False)