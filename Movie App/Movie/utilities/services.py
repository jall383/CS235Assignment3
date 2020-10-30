
import random
import Movie.adapters.data.memory as memory


def get_random_movies(num):
    full_mov = memory.memory_instance.get_movie_list()
    rand_lst = []
    if num >= len(full_mov):
        num = num - 1
    for x in range(0, num):
        rand_id = random.randint(0, len(full_mov)-1)
        rand_lst.append(full_mov[rand_id])

    return rand_lst


