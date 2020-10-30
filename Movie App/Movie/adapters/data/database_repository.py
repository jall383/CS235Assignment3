import csv
import os

from datetime import date
from typing import List

from sqlalchemy import desc, asc
from sqlalchemy.engine import Engine
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from werkzeug.security import generate_password_hash

from sqlalchemy.orm import scoped_session
from flask import _app_ctx_stack

from Movie.Domain.A1_Main import User, Review, Movie, Genre, Actor, Director, MovieFileCSVReader, WatchList
from Movie.adapters.data.memory import Memory_Repository

tags = None


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        # this method can be used e.g. to allow Flask to start a new session for each http request,
        # via the 'before_request' callback
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()


class SqlAlchemyRepository(Memory_Repository):
    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def add_user(self, user: User):
        with self._session_cm as scm:
            scm.session.add(user)
            scm.commit()

    def add_movie(self, movie: Movie):
        with self._session_cm as scm:
            scm.session.add(movie)
            scm.commit()

    def add_genre(self, genre : Genre):
        with self._session_cm as scm:
            scm.session.add(genre)
            scm.commit()

    def add_review(self, review, movie, user):
        with self._session_cm as scm:
            scm.session.add(review)
            scm.commit()

    def get_user(self, username):
        user = None
        try:
            user = self._session_cm.session.query(User).filter(username == user_name).one()
        except NoResultFound:
            pass

        return user

    def get_movie_list(self):
        movie_lst = self._session_cm.session.query(Movie).all()
        return movie_lst

    def get_actor_list(self):
        actor_list = self._session_cm.session.query(Actor).all()
        return actor_list

    def get_genre_list(self):
        gen_lst = self._session_cm.session.query(Genre).all()
        return gen_lst

    def get_director_list(self):
        dir_lst  = self._session_cm.session.query(Director).all()








