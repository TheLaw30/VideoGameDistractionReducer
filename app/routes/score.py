# These routes are an example of how to use data, forms and routes to create
# a blog where a blogs and comments on those blogs can be
# Created, Read, Updated or Deleted (CRUD)

from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import require_role, Scoreboard
from app.classes.forms import ScoreForm
from flask_login import login_required
import datetime as dt

# This is the route to list all blogs
@app.route('/score')
@app.route('/score')
# This means the user must be logged in to see this page
@login_required
def scoreList():
    # This retrieves all of the 'blogs' that are stored in MongoDB and places them in a
    # mongoengine object as a list of dictionaries name 'blogs'.
    scores = Scoreboard.objects()
    # This renders (shows to the user) the blogs.html template. it also sends the blogs object 
    # to the template as a variable named blogs.  The template uses a for loop to display
    # each blog.
    return render_template('score.html',scores=scores)

# This route will get one specific blog and any comments associated with that blog.  
# The blogID is a variable that must be passsed as a parameter to the function and 
# can then be used in the query to retrieve that blog from the database. This route 
# is called when the user clicks a link on bloglist.html template.
# The angle brackets (<>) indicate a variable. 
@app.route('/score/<scoreID>')
# This route will only run if the user is logged in.
@login_required
def score(scoreID):
    # retrieve the blog using the blogID
    thisScore = Scoreboard.objects.get(id=scoreID)
    # If there are no comments the 'comments' object will have the value 'None'. Comments are 
    # related to blogs meaning that every comment contains a reference to a blog. In this case
    # there is a field on the comment collection called 'blog' that is a reference the Blog
    # document it is related to.  You can use the blogID to get the blog and then you can use
    # the blog object (thisBlog in this case) to get all the comments.
    # Send the blog object and the comments object to the 'blog.html' template.
    return render_template('score.html',score=thisScore)

# This route actually does two things depending on the state of the if statement 
# 'if form.validate_on_submit()'. When the route is first called, the form has not 
# been submitted yet so the if statement is False and the route renders the form.
# If the user has filled out and succesfully submited the form then the if statement
# is True and this route creates the new blog based on what the user put in the form.
# Because this route includes a form that both gets and blogs data it needs the 'methods'
# in the route decorator.
@app.route('/score', methods=['GET', 'POST'])
# This means the user must be logged in to see this page
@login_required
# This is a function that is run when the user requests this route.
def scoreNew():
    # This gets the form object from the form.py classes that can be displayed on the template.
    form = ScoreForm()

    # This is a conditional that evaluates to 'True' if the user submitted the form successfully.
    # validate_on_submit() is a method of the form object. 
    if form.validate_on_submit():

        # This stores all the values that the user entered into the new blog form. 
        # Blog() is a mongoengine method for creating a new blog. 'newBlog' is the variable 
        # that stores the object that is the result of the Blog() method.  
        newScore = Scoreboard(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            score = form.score.data,
            HighScores = form.HighScores.data,
            TypeOfTest = form.TypeOfTest.data,
            author = current_user.id,
            # This sets the modifydate to the current datetime.
            modify_date = dt.datetime.utcnow
        )
        # This is a method that saves the data to the mongoDB database.
        newScore.save()

        # Once the new blog is saved, this sends the user to that blog using redirect.
        # and url_for. Redirect is used to redirect a user to different route so that 
        # routes code can be run. In this case the user just created a blog so we want 
        # to send them to that blog. url_for takes as its argument the function name
        # for that route (the part after the def key word). You also need to send any
        # other values that are needed by the route you are redirecting to.
        return redirect(url_for('score',scoreID=newScore.id))

    # if form.validate_on_submit() is false then the user either has not yet filled out
    # the form or the form had an error and the user is sent to a blank form. Form errors are 
    # stored in the form object and are displayed on the form. take a look at blogform.html to 
    # see how that works.
    return render_template('score.html',form=form)


# the routes below are the CRUD for the comments that are related to the blogs. This
# process is exactly the same as for blogs with one addition. Each comment is related to
# a specific blog via a field on the comment called 'blog'. The 'blog' field contains a 
# reference to the Blog document. See the @app.route('/blog/<blogID>') above for more details
# about how comments are related to blogs.  Additionally, take a look at data.py to see how the
# relationship is defined in the Blog and the Comment collections.
