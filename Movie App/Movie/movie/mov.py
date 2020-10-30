from datetime import date
from flask import Blueprint, render_template, redirect, url_for, session, request, flash
import Movie.movie.services as services
from wtforms import TextAreaField
from Movie.Home.home import home
import Movie.utilities.utilities as utilities
import Movie.movie.services as services
# Configure Blueprint.
mov_blueprint: Blueprint = Blueprint('mov_bp', __name__)



@mov_blueprint.route('/browse/name')
def browse_by_name():
    return render_template('movie/Browse.html', list_of_movies=services.get_movies_by_name(),
                           message="Browse all of our Movies in Name order", search_val=True, watchlist=utilities.get_watchlist())


@mov_blueprint.route('/browse/name', methods=['POST'])
def name_search():
    text = request.form['text']
    if text == "":
        return browse_by_name()
    else:
        search_results = services.search_name(text)
        return render_template('movie/Browse.html', list_of_movies=search_results,
                               message=f"Browsing all movies related to {text.capitalize()}", search_val=True, watchlist=utilities.get_watchlist())


@mov_blueprint.route('/browse/genre')
def browse_by_genre():
    genres = services.get_genres()
    genres.sort()
    return render_template('movie/genre_page.html', list_of_genres=genres, watchlist=utilities.get_watchlist())


@mov_blueprint.route('/browse/genre/<gen_of_choice>', methods=['GET'])
def show_movies_in_genre(gen_of_choice):
    chosen_movie_list = services.get_movies_from_genre(gen_of_choice)
    chosen_movie_list.sort()
    return render_template('movie/browse_gen.html', list_of_movies=chosen_movie_list,
                           message=f"Browsing all {gen_of_choice} Movies ", watchlist=utilities.get_watchlist())


@mov_blueprint.route('/browse/genre/<genre>', methods=['POST'])
def gen_name_search(genre):
    text = request.form['text']
    if text == "":
        return browse_by_name()
    else:
        search_results = services.search_genre(text, genre)
        return render_template('movie/Browse_gen.html', list_of_movies=search_results,
                               message=f"{genre} movies related to {text.capitalize()}", search_val=True, watchlist=utilities.get_watchlist())


@mov_blueprint.route('/browse/actor')
def browse_by_actor():
    actors = services.get_actors()
    actors.sort()
    return render_template('movie/actor_page.html', message="Browsing all Actors", list_of_actors=actors, watchlist=utilities.get_watchlist())


@mov_blueprint.route('/browse/actor/<act_of_choice>', methods=['GET'])
def show_movies_from_actor(act_of_choice):
    chosen_movie_list = services.get_movies_from_actor(act_of_choice)
    chosen_movie_list.sort()
    return render_template('movie/browse.html', list_of_movies=chosen_movie_list,
                           message=f"Browsing all Movies starring {act_of_choice}", search_val=False, watchlist=utilities.get_watchlist())


@mov_blueprint.route('/browse/actor', methods=['POST'])
def actor_search():
    text = request.form['text']
    if text == "":
        return browse_by_actor()
    else:
        search_results = services.search_actor(text)
        return render_template('movie/actor_page.html', message=f"Actors related to {text.capitalize()}",
                               list_of_actors=search_results, watchlist=utilities.get_watchlist())


@mov_blueprint.route('/browse/director')
def browse_by_director():
    directors = services.get_directors()
    directors.sort()
    return render_template('movie/dir_page.html', message=f"Browsing all Directors", list_of_directors=directors, watchlist=utilities.get_watchlist())


@mov_blueprint.route('/browse/director/<dir_of_choice>', methods=['GET'])
def show_movies_from_director(dir_of_choice):
    chosen_movie_list = services.get_movies_from_director(dir_of_choice)
    chosen_movie_list.sort()
    return render_template('movie/browse.html', list_of_movies=chosen_movie_list,
                           message=f"Browsing all Movies directed by {dir_of_choice}", search_val=False, watchlist=utilities.get_watchlist())


@mov_blueprint.route('/browse/director', methods=['POST'])
def director_search():
    text = request.form['text']
    if text == "":
        return browse_by_director()
    else:
        search_results = services.search_director(text)
        return render_template('movie/dir_page.html', message=f"Directors related to {text.capitalize()}",
                               list_of_directors=search_results, watchlist=utilities.get_watchlist())


@mov_blueprint.route('/browse/movie/<hyperlink>')
def show_movie(hyperlink):
    rev_tr = False
    mov = services.get_movie(hyperlink)
    reviews = mov.get_reviews()
    if not len(reviews):
        rev_tr = True
    return render_template('movie/movie_disp.html', rev_tr=rev_tr, reviews=reviews, title="Movie Details", movie=mov, watchlist=utilities.get_watchlist())


@mov_blueprint.route('/browse/movie/add/<movie>')
def add_to_list(movie):
    mov = services.get_movie(movie)
    try:
        if 'username' in session:
            user = services.get_user(session['username'])
            user.watch_movie(mov)
    except ValueError:
        session.clear()
    except AttributeError:
        session.clear()
    return show_movie(mov.hyperlink)


@mov_blueprint.route('/browse/movie/<hyperlink>', methods=['GET', 'POST'])
def add_review(hyperlink):
    text = request.form['text']
    if text == "":
        return show_movie(hyperlink)
    else:
        try:
            mov = services.get_movie(hyperlink)
            services.add_review_for_current_user(mov, text, session['username'])
            return show_movie(hyperlink)
        except ValueError:
            session.clear()
            return redirect(url_for('home_bp.home'))


@mov_blueprint.route('/browse/movie/add/<hyperlink>', methods=['GET', 'POST'])
def add_review_v2(hyperlink):
    text = request.form['text']
    if text == "":
        return show_movie(hyperlink)
    else:
        try:
            mov = services.get_movie(hyperlink)
            services.add_review_for_current_user(mov, text, session['username'])
            return show_movie(hyperlink)
        except ValueError:
            session.clear()
            return redirect(url_for('home_bp.home'))