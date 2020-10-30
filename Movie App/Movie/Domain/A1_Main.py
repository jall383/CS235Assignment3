from datetime import datetime
import csv


##########################################
########  IMPROVED USER CLASS  ###########
##########################################
class User:
    def __init__(self, username_full: str, password_full: str):
        self.__total_time_watched = 0
        self.__movie_review_list = []
        self.__watched_movies_list = []
        if username_full == "" or type(username_full) is not str or password_full == "" or type(
                password_full) is not str:
            self.__username = None
            self.__password = None
        else:
            username_full.strip()
            self.__username = username_full
            self.__password = password_full
        self.to_watch_list = WatchList(self.__username)

    @property
    def user_name(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies_list

    @property
    def reviews(self):
        return self.__movie_review_list

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__total_time_watched

    @property
    def watchlist(self):
        return self.to_watch_list

    def __repr__(self):
        return f"<User {self.__username}>"

    def __eq__(self, other):
        if self.__username == other.__username:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__username < other.__username:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__username)

    def watch_movie(self, movie):
        if movie not in self.__watched_movies_list:
            self.__watched_movies_list.append(movie)
        self.__total_time_watched += movie.runtime_minutes
        if movie in self.to_watch_list:
            self.to_watch_list.remove_movie(movie)

    def watch_first_movie(self):
        self.watch_movie(self.to_watch_list.first_movie_in_watchlist())

    def add_to_watch_later(self, movie):
        if type(movie) is Movie:
            self.to_watch_list.add_movie(movie)

    def add_review(self, review):
        self.__movie_review_list.append(review)

    def total_watchlist_movie_length(self):
        total = 0
        for movie in self.to_watch_list:
            total += movie.runtime_minutes
        return total


###################################
########  REVIEW CLASS  ###########
###################################

class Review:
    def __init__(self, movie_name_full: str, review_text_full: str, reviewed_by: str):
        self.__movie_rating = None
        self.__review_time = datetime.now()
        self.__user_reviewed = reviewed_by
        if type(movie_name_full) is not Movie:
            self.__movie_name = Movie("Null", 0000)
        else:
            self.__movie_name = movie_name_full

        if review_text_full == "" or type(review_text_full) is not str:
            self.__review_text = None

        else:
            self.__review_text = review_text_full.strip()

    def get_username(self):
        return self.__user_reviewed


    @property
    def movie(self) -> str:
        return self.__movie_name

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__movie_rating

    @property
    def timestamp(self) -> str:
        return f"{self.__review_time.day}/{self.__review_time.month}/{self.__review_time.year}"

    def __repr__(self):
        return f"Review {self.__movie_name}, {self.__review_text}"

    def __eq__(self, other):
        if self.__movie_name == other.__movie_name and self.__review_text == other.__review_text:
            return True
        else:
            return False


##################################
########  MOVIE CLASS  ###########
##################################

class Movie:
    def __init__(self, movie_name_full: str, movie_year_full: int, movie_id: int):
        self._runtime_in_minutes = 0
        self._genres_list = []
        self._actors_list = []
        self._ID = movie_id
        self._title = None
        self._description = None
        self._director = None
        self._reviews = []
        if movie_name_full == "" or type(movie_name_full) is not str:
            self.__movie_name = None
            self.__movie_year = None
        else:
            if movie_year_full < 1900 or type(movie_year_full) is not int:
                self.__movie_name = None
                self.__movie_year = None
            else:
                self.__movie_name = movie_name_full.strip()
                self.__movie_year = movie_year_full
                if "/" not in self.__movie_name:
                    self.__hyperlink = f"{self._ID}{self.__movie_name}{self.__movie_year}"
                else:
                    #If there is a "/" in the name, the hyperlink is wrong, so if one exists, this code removes it from the hyperlink
                    temp = self.__movie_name
                    let = ""
                    for x in range(0, len(temp)):
                        if temp[x] != "/":
                            let += temp[x]
                    self.__hyperlink = f"{self._ID}{let}{self.__movie_year}"

    # Title
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value):
        if type(value) is str:
            self._title = value.strip()

    def add_review(self, review):
        self._reviews.append(review)

    def get_reviews(self):
        return self._reviews

    @property
    def year(self):
        return self.__movie_year

    def get_year(self):
        return f"{self.__movie_year}"

    def get_name(self):
        return f"{self.__movie_name}"

    def get_id(self):
        return self._ID

    @property
    def hyperlink(self) -> str:
        return self.__hyperlink

    # Director
    @property
    def director(self) -> str:
        return self._director

    def set_director(self, value):
        if type(value) is Director:
            if self._director is None:
                self._director = value

    # Description
    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value):
        if type(value) is str:
            self._description = value.strip()

    # Actors
    @property
    def actors(self):
        return self._actors_list

    @actors.setter
    def actors(self, actor):
        if type(actor) is list:
            self._actors_list = actor

    # Genres
    @property
    def genres(self):
        return self._genres_list

    @genres.setter
    def genres(self, genre):
        if type(genre) is list:
            self._genres_list = genre

    @property
    def runtime_minutes(self):
        return self._runtime_in_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime):
        if type(runtime) is int:
            if runtime > 0:
                self._runtime_in_minutes = runtime
            else:
                raise ValueError()
        else:
            raise ValueError()

    def __repr__(self):
        return f"MOVIE {self.__movie_name}  |    YEAR {self.__movie_year}"

    def __eq__(self, other):
        if self.__movie_name == other.__movie_name and self.__movie_year == other.__movie_year:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__movie_name < other.__movie_name:
            return True
        elif self.__movie_name == other.__movie_name and self.__movie_year < other.__movie_year:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__movie_name + str(self.__movie_year))

    def add_actor(self, actor):
        self._actors_list.append(actor)

    def remove_actor(self, actor):
        if actor in self._actors_list:
            self._actors_list.remove(actor)

    def add_genre(self, genre):
        self._genres_list.append(genre)

    def remove_genre(self, genre):
        if genre in self._genres_list:
            self._genres_list.remove(genre)

    def get_actor(self):
        return self._actors_list

    def get_genre(self):
        return self._genres_list

    def get_director(self):
        return self._director


##################################
########  GENRE CLASS  ###########
##################################

class Genre:
    def __init__(self, genre_name_full: str):
        self.__movies = []
        if genre_name_full == "" or type(genre_name_full) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name_full.strip()
        self.__hyperlink = f"{self.__genre_name}"

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    @property
    def hyperlink(self) -> str:
        return self.__hyperlink

    def add_mov(self, mov):
        self.__movies.append(mov)

    def get_mov(self):
        return self.__movies

    def __repr__(self):
        return f"{self.__genre_name}"

    def __eq__(self, other):
        if self.__genre_name == other.__genre_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__genre_name < other.__genre_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__genre_name)


##################################
########  ACTOR CLASS  ###########
##################################

class Actor:
    def __init__(self, actor_name_full: str):
        self.colleague_list = []
        self.__movies = []

        if actor_name_full == "" or type(actor_name_full) is not str:
            self.__actor_name = None
        else:
            self.__actor_name = actor_name_full.strip()
        self.__hyperlink = f"{self.__actor_name}"

    @property
    def actor_full_name(self) -> str:
        return self.__actor_name

    @property
    def hyperlink(self) -> str:
        return self.__hyperlink

    def add_mov(self, mov):
        self.__movies.append(mov)

    def get_mov(self):
        return self.__movies

    def __repr__(self):
        return f"{self.__actor_name}"

    def __eq__(self, other):
        if self.__actor_name == other.__actor_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__actor_name < other.__actor_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__actor_name)

    def add_actor_colleague(self, colleague):
        self.colleague_list.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.colleague_list:
            return True
        else:
            return False


#####################################
########  DIRECTOR CLASS  ###########
#####################################

class Director:
    def __init__(self, director_full_name: str):
        self.__movies = []
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()
        self.__hyperlink = f"{self.__director_full_name}"

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    @property
    def hyperlink(self) -> str:
        return self.__hyperlink

    def add_mov(self, mov):
        self.__movies.append(mov)

    def get_mov(self):
        return self.__movies

    def __repr__(self):
        return f"{self.__director_full_name}"

    def __eq__(self, other):
        if self.__director_full_name == other.__director_full_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__director_full_name < other.__director_full_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__director_full_name)


##################################################
########  MOVIE FILE CSV READER CLASS  ###########
##################################################

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.genre_dataset = []
        self.actor_dataset = []
        self.director_dataset = []
        self.movie_dataset = []
        self.__file_name = file_name

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                self.dataset_of_movies_setter(row)
                self.dataset_of_actors_setter(row)
                self.dataset_of_directors_setter(row)
                self.dataset_of_genres_setter(row)
                index += 1

    @property
    def dataset_of_movies(self):
        return self.movie_dataset

    def dataset_of_movies_setter(self, row):
        temp_mov = (Movie(row['Title'], int(row['Year']), int(row['Rank'])))
        act_lst = row['Actors'].split(",")
        for actor in act_lst:
            act = Actor(actor)
            temp_mov.add_actor(act)
        dir = Director(row["Director"])
        temp_mov.set_director(dir)
        gen_lst = row['Genre'].split(",")
        for genre in gen_lst:
            gen = Genre(genre)
            temp_mov.add_genre(gen)

        self.movie_dataset.append(temp_mov)

    @property
    def dataset_of_actors(self):
        return self.actor_dataset

    def dataset_of_actors_setter(self, row):
        act_lst = row['Actors'].split(",")
        for actor in act_lst:
            act = Actor(actor)
            if act not in self.actor_dataset:
                self.actor_dataset.append(Actor(actor))

    @property
    def dataset_of_directors(self):
        return self.director_dataset

    def dataset_of_directors_setter(self, row):
        dir = Director(row["Director"])
        if dir not in self.director_dataset:
            self.director_dataset.append(Director(row['Director']))

    @property
    def dataset_of_genres(self):
        return self.genre_dataset

    def dataset_of_genres_setter(self, row):
        gen_lst = row['Genre'].split(",")
        for genre in gen_lst:
            gen = Genre(genre)
            if gen not in self.genre_dataset:
                self.genre_dataset.append(Genre(genre))


###############      ####          ####      ####################       ###############      #####       ####          #######          ##################          #########         #####       ####
###############       ####        ####       ####################       ###############      ######      ####        ###########        ##################        #############       ######      ####
####                   ####      ####                ####               ####                 #######     ####      #####     #####             ####              #####     #####      #######     ####
####                    ####    ####                 ####               ####                 ########    ####      ####                        ####              ####       ####      ########    ####
####                     ####  ####                  ####               ####                 #### ####   ####       ####                       ####              ####       ####      #### ####   ####
#########                 ########                   ####               #########            ####  ####  ####         #####                    ####              ####       ####      ####  ####  ####
#########                 ########                   ####               #########            ####   #### ####             #####                ####              ####       ####      ####   #### ####
####                     ####  ####                  ####               ####                 ####    ########                ####              ####              ####       ####      ####    ########
####                    ####    ####                 ####               ####                 ####     #######                 ####             ####              ####       ####      ####     #######
####                   ####      ####                ####               ####                 ####      ######      #####     #####             ####              #####     #####      ####      ######
################      ####        ####               ####               ###############      ####       #####        ###########        ###################       #############       ####       #####
################     ####          ####              ####               ###############      ####        ####          #######          ###################         #########         ####        ####

# (Wow that took way too long to make)#


###############################################
########  IMPROVED WATCHLIST CLASS  ###########
###############################################

class WatchList:
    def __init__(self, user):
        self.__watch_list = []
        self.__watch_list_owner = user

    def add_movie(self, movie):
        if type(movie) is Movie and movie not in self.__watch_list:
            self.__watch_list.append(movie)

    def remove_movie(self, movie):
        if movie in self.__watch_list:
            self.__watch_list.remove(movie)

    def select_movie_to_watch(self, index):
        if type(index) is int and 0 <= index < len(self.__watch_list):
            return self.__watch_list[index]

    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        if len(self.__watch_list) > 0:
            return self.__watch_list[0]
        else:
            return None

    def __iter__(self):
        return iter(self.__watch_list)

    def __next__(self, itr_lst):
        return itr_lst.__next__()
