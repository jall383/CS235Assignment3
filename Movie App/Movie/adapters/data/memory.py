import csv
import os
from datetime import date, datetime
from Movie.Domain.A1_Main import User, Review, Movie, Genre, Actor, Director, MovieFileCSVReader, WatchList

memory_instance = None

def get_genres_from_movies(mov_list):
    gen_list = []
    for movie in mov_list:
        for genre in movie.get_genre():
            if genre not in gen_list:
                genre.add_mov(movie)
                gen_list.append(genre)
            else:
                x = gen_list.index(genre)
                gen_list[x].add_mov(movie)
    return gen_list


def get_actors_from_movies(mov_list):
    act_list = []
    for movie in mov_list:
        for actor in movie.get_actor():
            if actor not in act_list:
                actor.add_mov(movie)
                act_list.append(actor)
            else:
                x = act_list.index(actor)
                act_list[x].add_mov(movie)
    return act_list


def get_director_from_movies(mov_list):
    dir_list = []
    for movie in mov_list:
        if movie.get_director() is None:
            pass
        elif movie.get_director() not in dir_list:
            movie.get_director().add_mov(movie)
            dir_list.append(movie.get_director())
        elif movie.get_director() in dir_list:
            x = dir_list.index(movie.get_director())
            dir_list[x].add_mov(movie)
    return dir_list


class Memory_Repository:
    def __init__(self):
        self.__movies = []
        self.__users = []
        temp_mov = MovieFileCSVReader("Data1000Movies.csv")
        temp_mov.read_csv_file()
        self.__movies = temp_mov.dataset_of_movies
        self.__genres = get_genres_from_movies(self.__movies)
        self.__actors = get_actors_from_movies(self.__movies)
        self.__directors = get_director_from_movies(self.__movies)

    def get_movie_list(self):
        return self.__movies

    def get_actor_list(self):
        return self.__actors

    def get_genre_list(self):
        return self.__genres

    def get_director_list(self):
        return self.__directors

    def add_to_watchlist(self, movie, user):
        x = self.__users.index(user)
        self.__users[x].watched_movies.append(movie)

    def add_user(self, user):
        self.__users.append(user)

    def add_genre(self, genre):
        self.__genres.append(genre)

    def add_movie(self, movie):
        self.__movies.append(movie)

    def get_user(self, username):
        user = None
        for us in self.__users:
            if us.user_name == username:
                user = us
        return user

    def add_review(self, review, movie, user):
        x = self.__movies.index(movie)
        y = self.__users.index(user)
        if review not in self.__users[y].reviews:
            self.__users[y].add_review(review)
            self.__movies[x].add_review(review)