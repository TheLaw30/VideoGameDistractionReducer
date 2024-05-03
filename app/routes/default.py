from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/z_start_game')
def startgame():
    return render_template('z_start_game.html')

@app.route('/z_reading')
def reading():
    return render_template('z_reading.html')

@app.route('/z_math')
def math():
    return render_template('/')

@app.route('/z_math_option1')
def math_option1():
    return render_template('z_math_option1.html')


@app.route('/z_math_option1_of_option1')
def Math_option1_of_option1():
    return render_template('z_math_option1_of_option1.html')    

@app.route('/z_math3')
def math3():
    return render_template('z_math3.html')
@app.route('/z_math4')
def math4():
    return render_template('z_math4.html')
@app.route('/z_reading1')
def reading1():
    return render_template('z_reading1.html')
@app.route('/z_reading2')
def reading2():
    return render_template('z_reading2.html')
@app.route('/z_reading3')
def reading3():
    return render_template('z_reading3.html')
@app.route('/z_reading4')
def reading4():
    return render_template('z_reading4.html')
@app.route('/score')
def score():
    return render_template('score.html')
# @app.route('/start_game')
# def startgame():
#     return render_template('start_game.html')
@app.route('/score')
def mathquizlist():
    return render_template('z_mathquiz.html')