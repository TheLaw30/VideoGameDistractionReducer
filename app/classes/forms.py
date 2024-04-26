# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from random import randint
from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField

class MathQuizForm(FlaskForm):
    question_1 = StringField('What is 24+19?')
    question_2 = StringField('What is 4 x 90?')
    question_3 = StringField('What is 51/17?')
    question_4 = StringField('What is 5^3?')
    question_5 = StringField("What is d/dx x^3?")    

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role', choices=[("Teacher","Teacher"),("Student","Student")])
    level_M = SelectField('Math Level', choices=[('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),('5', '5')])
    level_R = SelectField('Lexile Score', choices=[('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),('5', '5')])
    favorite_Food = SelectField('food', choices=[('tacos', 'tacos'), ('burritos', 'burritos')])

class GameForm(FlaskForm):
    name = StringField('Game Name', validators=[DataRequired()])
    price = IntegerField('Game Price', validators=[DataRequired()])
    age = IntegerField('Game Age')
    submit = SubmitField('Game')

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class ClinicForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    streetAddress = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = StringField('Zipcode',validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
