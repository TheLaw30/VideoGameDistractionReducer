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
    return render_template('z_math.html')

@app.route('/z_math_option1')
def math_option1():
    return render_template('z_math_option1.html')

@app.route('/z_math_option2')
def math_option2():
    return render_template('z_math_option2.html')
# @app.route('/start_game')
# def startgame():
#     return render_template('start_game.html')