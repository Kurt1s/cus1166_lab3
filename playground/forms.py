from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired

class NewCourseForm(FlaskForm):
    class_id = IntegerField('Class ID: ', validators = [DataRequired()])
    course_num = IntegerField('Course number: ', validators = [DataRequired()])
    course_name = IntegerField('Course name: ', validators = [DataRequired()])
    submit = SubmitField('submit')

class RegisteredStudent(FlaskForm):
    student_id = IntegerField('Student ID: ', validators = [DataRequired()])
    student_grade = IntegerField('Student grade: ', validators = [DataRequired()])
    student_name = IntegerField('Student name: ', validators = [DataRequired()])
    submit = SubmitField('submit')