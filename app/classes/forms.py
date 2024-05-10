# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from random import randint
from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired, EqualTo
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField


a = randint(-50,50)
b = randint(-10,10)
c = randint(-3,-1)
d = randint(1, 30)
e = randint(1,5)
f = randint(12,30)

class MathQuizForm(FlaskForm):
    question_1 = SelectField('What is ' + str(a) + "+" + str(b) + '?', choices=[(c+e, c+e), (a+b, a+b),(e-a, e-a), (a+c, c+a),(a*b, a*b)])
    question_2 = SelectField('What is ' + str(c) + " x" + str(d) + '?', choices=[(c+e, c+e), (a*b, a*b),(e-a, e-a), (d*c, c*d),(a*b, a*b)])
    question_3 = SelectField('What is ' + str(e) + "^" + str(e) + '?', choices=[(c**e, c**e), (e**a, e**a),(e-a, e-a), (a+a, a+a),(e**e, e**e)])
    question_4 = SelectField('What is ' + str(b) + "/" + str(c) + '?', choices=[(b/c, b/c), (a*b, a*b),(e/a, e/a), (d*e, d*e),(a/b, a/b)])
    question_5 = SelectField('What is the remainder of ' + str(f) + '/' + str(e) + '?', choices=[(f%e, f%e), (e/d, e/d), (e+a , e+a)])    
    
    submit = SubmitField('Submit')


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
    comment = StringField('Your comments', validators=[DataRequired()])
    rating = IntegerField('Rate out of 5')
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

class ScoreForm(FlaskForm):
    myscore = IntegerField()
    HighScores = StringField()
    TypeOfTest = StringField()
    submit = SubmitField('Submit')