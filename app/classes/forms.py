# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from random import randint
from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired, EqualTo
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField


a = randint(-50,50)
b = randint(1,10)
c = randint(1,2)
d = randint(-30, 30)
e = randint(-5,5)

class MathQuizForm(FlaskForm):
    ans_1 = a + b
    ans_2 = c * d
    question_1 = IntegerField('What is ' + str(a) + "+" + str(b) + '?', validators=[EqualTo(ans_1, 'Answer is incorrect')])
    question_2 = StringField('What is ' + str(c) + " x" + str(d) + '?', validators=[EqualTo(ans_2, 'Answer is incorrect')])
    question_3 = StringField('What is ' + str(e) + "^" + str(e) + '?', validators=[EqualTo(int(e^e), 'Answer is incorrect')])
    question_4 = StringField('What is ' + str(b) + "/" + str(c) + '?', validators=[EqualTo(int(b/c), 'Answer is incorrect')])
    question_5 = StringField('What is d/dx x^' + str(e) + '?', validators=[DataRequired()])    
    
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
    score = 0
    HighScores = StringField()
    TypeOfTest = StringField()
