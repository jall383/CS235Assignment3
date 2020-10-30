from datetime import date, datetime
from typing import List

import pytest
from Movie.Domain.A1_Main import User, Movie, Genre, Review
import Movie.adapters.data.memory as memory

memory.memory_instance = memory.Memory_Repository()



@pytest.fixture()
def repo():
    return memory.memory_instance



def test_repository_can_add_a_user(repo):
    user = User('Dave', '123456789')

    repo.add_user(user)
    repo.add_user(User('fmercury', '8734gfe2058v'))
    assert repo.get_user('Dave') is user


def test_repository_can_retrieve_a_user(repo):
    user = repo.get_user('fmercury')
    assert user == User('fmercury', '8734gfe2058v')


def test_repository_does_not_retrieve_a_non_existent_user(repo):
    user = repo.get_user('prince')
    assert user is None


def test_repository_can_add_movie(repo):
    movie = Movie("MovieName", 2015, 1)
    repo.add_movie(movie)
    assert repo.get_movie_list()[-1] is movie


def test_repository_can_retrieve_movie(repo):
    movie = repo.get_movie_list()[-1]
    # Check that the Article has the expected title.
    assert movie.get_name() == 'MovieName'


def test_repository_can_add_a_genre(repo):
    genre = Genre('Action')
    repo.add_genre(genre)

    assert genre in repo.get_genre_list()


def test_repository_can_retrieve_genres(repo):
    genres = repo.get_genre_list()
    genre = Genre('Action')
    assert genre in genres



