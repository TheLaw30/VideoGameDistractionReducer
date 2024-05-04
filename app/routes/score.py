# These routes are an example of how to use data, forms and routes to create
# a blog where a blogs and comments on those blogs can be
# Created, Read, Updated or Deleted (CRUD)

from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import require_role, Score
from app.classes.forms import ScoreForm
from flask_login import login_required
import datetime as dt

@app.route('/scores/list')
@app.route('/scores')


@login_required
def scoreList():
   scores = Score.objects()
   return render_template('scores.html',scores=scores)

@app.route('/score/new', methods=['GET', 'POST'])
@login_required
def scoreNew():
    form = ScoreForm()
    if form.validate_on_submit():
        newScore = Score(
            myscore = form.myscore.data,
            HighScores = form.HighScores.data,
            TypeOfTest = form.TypeOfTest.data,
            author = current_user.id,
            modify_date = dt.datetime.utcnow
        )
        newScore.save()
        return redirect(url_for('score2', scoreID=newScore.id))

    return render_template('scoreform.html', form=form)


@app.route('/score/<scoreID>')
@login_required
def score2(scoreID):
    thisScore = Score.objects.get(id=scoreID)
    return render_template('score.html',score=thisScore)
