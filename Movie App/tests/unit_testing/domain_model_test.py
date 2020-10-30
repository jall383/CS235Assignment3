from datetime import date

from Movie.Domain.A1_Main import User, Movie, Genre, Review

import pytest


@pytest.fixture()
def user():
    return User('dbowie', '1234567890')


@pytest.fixture()
def movie():
    return Movie("MovieName", 2015, 1)


@pytest.fixture()
def genre():
    return Genre("Action")


def test_user_construction(user):
    assert user.user_name == 'dbowie'
    assert user.password == '1234567890'
    assert repr(user) == '<User dbowie>'

    for review in user.reviews:
        # User should have an empty list of Comments after construction.
        assert False


def test_movie_construction(movie):
    assert movie.hyperlink == "1MovieName2015"
    assert movie.get_name() == 'MovieName'
    assert movie.year == 2015
    assert movie.runtime_minutes == 0
    assert repr(movie) == "MOVIE MovieName  |    YEAR 2015"


def test_make_review(movie, user):
    review_text = 'COVID-19 in the USA!'
    review = Review(movie, review_text, user)
    user.add_review(review)

    # Check that the User object knows about the Comment.
    assert review in user.reviews


def test_make_genre_associations(movie, genre):
    movie.add_genre(genre)
    genre.add_mov(movie)
    # Check that the movie knows about the genre.
    assert movie.genres[0] == genre
    # check that the genre knows about the movie.
    assert genre.get_mov()[0] == movie
