import Movie.adapters.data.memory as memory
import Movie.authentication.services as aut_services
from Movie.Domain.A1_Main import User, Review, Movie, Genre, Actor, Director, MovieFileCSVReader, WatchList


def get_user(username):
    return memory.memory_instance.get_user(username)


def get_movies_by_name():
    full_mov = memory.memory_instance.get_movie_list()
    full_mov.sort()
    return full_mov



def get_movie(mov_id):
    full_mov = memory.memory_instance.get_movie_list()
    for movie in full_mov:
        if movie.hyperlink == mov_id:
            return movie
    return None


def get_genres():
    gen_list = memory.memory_instance.get_genre_list()
    return gen_list


def get_movies_from_genre(genre):
    gen_list = memory.memory_instance.get_genre_list()
    chosen_genre = None
    for gen in gen_list:
        if gen.genre_name == genre:
            chosen_genre = gen
    return chosen_genre.get_mov()


def get_actors():
    act_list = memory.memory_instance.get_actor_list()
    return act_list


def get_movies_from_actor(actor):
    act_list = memory.memory_instance.get_actor_list()
    chosen_actor = None
    for act in act_list:
        if act.actor_full_name == actor:
            chosen_actor = act
    return chosen_actor.get_mov()


def get_directors():
    dir_list = memory.memory_instance.get_director_list()
    return dir_list


def get_movies_from_director(director):
    dir_list = memory.memory_instance.get_director_list()
    chosen_director = None
    for dir in dir_list:
        if dir.director_full_name == director:
            chosen_director = dir
    return chosen_director.get_mov()


def search_name(query):
    movie_list = memory.memory_instance.get_movie_list()
    length = len(query)
    query = query.lower()
    similar_list = []
    same_list = []
    for movie in movie_list:
        name = movie.get_name()
        name = name.lower()
        if len(name) >= length:
            count = 0
            for let_I in range(0, length):
                if query[let_I] == name[let_I]:
                    count += 1
            if count == length:
                same_list.append(movie)
    same_list.sort()
    for movie in movie_list:
        name = movie.get_name()
        name = name.lower()
        if movie not in same_list:
            if query in name:
                similar_list.append(movie)
    similar_list.sort()
    return same_list + similar_list


def search_actor(query):
    actor_list = memory.memory_instance.get_actor_list()
    length = len(query)
    query = query.lower()
    similar_list = []
    same_list = []
    for actor in actor_list:
        name = actor.actor_full_name
        name = name.lower()
        if len(name) >= length:
            count = 0
            for let_I in range(0, length):
                if query[let_I] == name[let_I]:
                    count += 1
            if count == length:
                same_list.append(actor)
    same_list.sort()
    for actor in actor_list:
        name = actor.actor_full_name
        name = name.lower()
        if actor not in same_list:
            if query in name:
                similar_list.append(actor)
    similar_list.sort()
    return same_list + similar_list


def search_director(query):
    director_list = memory.memory_instance.get_director_list()
    length = len(query)
    query = query.lower()
    similar_list = []
    same_list = []
    for director in director_list:
        name = director.director_full_name
        name = name.lower()
        if len(name) >= length:
            count = 0
            for let_I in range(0, length):
                if query[let_I] == name[let_I]:
                    count += 1
            if count == length:
                same_list.append(director)
    same_list.sort()
    for director in director_list:
        name = director.director_full_name
        name = name.lower()
        if director not in same_list:
            if query in name:
                similar_list.append(director)
    similar_list.sort()
    return same_list + similar_list


def search_genre(query, gen_name):
    gen_list = memory.memory_instance.get_genre_list()
    genre = None
    for gen in gen_list:
        if gen.genre_name == gen_name:
            genre = gen
    movie_list = genre.get_mov()
    length = len(query)
    query = query.lower()
    similar_list = []
    same_list = []
    for movie in movie_list:
        name = movie.get_name()
        name = name.lower()
        if len(name) >= length:
            count = 0
            for let_I in range(0, length):
                if query[let_I] == name[let_I]:
                    count += 1
            if count == length:
                same_list.append(movie)
    same_list.sort()
    for movie in movie_list:
        name = movie.get_name()
        name = name.lower()
        if movie not in same_list:
            if query in name:
                similar_list.append(movie)
    similar_list.sort()
    return same_list + similar_list


def add_review_for_current_user(movie, rev, us):
    review = Review(movie, rev, us)
    user = memory.memory_instance.get_user(us)
    memory.memory_instance.add_review(review, movie, user)
