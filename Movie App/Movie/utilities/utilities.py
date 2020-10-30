from flask import Blueprint, render_template, redirect, url_for, session, request, flash

import Movie.utilities.services as services
import Movie.adapters.data.memory as memory

# Configure Blueprint.
utilities_blueprint = Blueprint('utilities_bp', __name__)


def get_selected_movies(num=10):
    movies = services.get_random_movies(num)
    return movies


def get_watchlist():
    try:
        if 'username' in session:
            watched = memory.memory_instance.get_user(session['username']).watched_movies
            return watched
        else:
            return []
    except AttributeError:
        return []
    except KeyError:
        return[]
