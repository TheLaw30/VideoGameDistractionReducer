from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Videogame
from app.classes.forms import GameForm
from flask_login import login_required
import datetime as dt

@app.route('/game/list')
@app.route('/games')
@login_required
def gameList():
     games = Videogame.objects()
     return render_template('games.html',games=games)


@app.route('/game/<gameID>')
@login_required
def game(gameID):
    thisGame = Videogame.objects.get(id=gameID)
    return render_template('game.html',game=thisGame)

@app.route('/game/delete/<gameID>')
@login_required
def gameDelete(gameID):
    deleteGame = Videogame.objects.get(id=gameID)
    if current_user == deleteGame.author:
        deleteGame.delete()
        flash('The Game was deleted.')
    else:
        flash("You can't delete a game you don't own.")
    games = Videogame.objects()  
    return render_template('games.html',games=games)

@app.route('/game/new', methods=['GET', 'POST'])
@login_required
def gameNew():
    form = GameForm()
    if form.validate_on_submit():
        newGame = Videogame(
            name = form.name.data,
            price = form.price.data,
            age = form.age.data,
            author = current_user.id,
            modify_date = dt.datetime.utcnow
        )
        newGame.save()

        return redirect(url_for('game',gameID=newGame.id))
    return render_template('gameform.html', form=form)





@app.route('/game/edit/<gameID>', methods=['GET', 'POST'])
@login_required
def gameEdit(gameID):
    editGame = Videogame.objects.get(id=gameID)
    if current_user != editGame.author:
        flash("You can't edit a game you don't own.")
        return redirect(url_for('game',gameID=gameID))
    form = GameForm()
    if form.validate_on_submit():
        editGame.update(
            name = form.name.data,
            price = form.price.data,
            age = form.age.data,
            modify_date = dt.datetime.utcnow
        )
        return redirect(url_for('game',gameID=gameID))

    form.name.data = editGame.name
    form.price.data = editGame.price
    form.age.data = editGame.age

    return render_template('gameform.html',form=form)

