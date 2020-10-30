import csv
import os
from datetime import date, datetime
from Movie.Domain.A1_Main import User, Review, Movie, Genre, Actor, Director, MovieFileCSVReader, WatchList
from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship

memory_instance = None
metadata = MetaData()

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False)
)

reviews = Table(
    'reviews', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', ForeignKey('users.id')),
    Column('movie_id', ForeignKey('movie.id')),
    Column('review', String(1024), nullable=False),
    Column('timestamp', DateTime, nullable=False)
)

movies = Table(
    'movies', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('date', Integer, nullable=False),
    Column('title', String(255), nullable=False),
    Column('hyperlink', String(255), nullable=False)
)

genres = Table(
    'genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(64), nullable=False)
)

actors = Table(
    'actors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(64), nullable=False)
)


def map_model_to_tables():
    mapper(User, users, properties={
        '__username': users.c.user_name,
        '__password': users.c.password,
        '__movie_review_list': relationship(Review, backref='_user')
    })
    mapper(Review, reviews, properties={
        '__review_text': reviews.c.review_text,
        '__review_time': reviews.c.timestamp
    })
    movie_mapper = mapper(Movie, movies, properties={
        '_ID': movies.c.get_id,
        '__movie_year': movies.c.get_year,
        '__movie_name': movies.c.get_name,
        '__hyperlink': movies.c.hyperlink,
        '_reviews': relationship(Review, backref='_article')
    })
    mapper(Genre, genres, properties={
        '__genre_name': genres.c.name,
        '__movies': relationship(
            movie_mapper,
            secondary=genres,
            backref="_genres_list"
        )
    })
