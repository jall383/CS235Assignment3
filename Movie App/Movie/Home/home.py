from flask import Blueprint, render_template, redirect, url_for, session, request

import Movie.utilities.utilities as utilities

home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    if 'username' in session:
        message = f"Here is a selection of movies we think you'll love {session['username']}!"
    else:
        message = "Here is a selection of movies we think you'll love!"
    return render_template('home/home.html', message=message,  selected_movies=utilities.get_selected_movies(), watchlist=utilities.get_watchlist())



@home_blueprint.route('/T&C')
def terms_and_conditions():
    return render_template("home/T_&_C.html")
