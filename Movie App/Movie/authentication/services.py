from werkzeug.security import generate_password_hash, check_password_hash

from Movie.adapters.data import memory
from Movie.Domain.A1_Main import User


class NameNotUniqueException(Exception):
    pass


class UnknownUserException(Exception):
    pass


class AuthenticationException(Exception):
    pass


def add_user(username: str, password: str):
    # Check that the given username is available.
    user = memory.memory_instance.get_user(username)
    if user is not None:
        raise NameNotUniqueException

    # Encrypt password so that the database doesn't store passwords 'in the clear'.
    password_hash = generate_password_hash(password)

    # Create and store the new User, with password encrypted.
    user = User(username, password_hash)
    memory.memory_instance.add_user(user)


def get_user(username: str):
    user = memory.memory_instance.get_user(username)
    if user is None:
        raise UnknownUserException
    return user_to_dict(user)


def authenticate_user(username: str, password: str):
    authenticated = False

    user = memory.memory_instance.get_user(username)
    if user is not None:
        authenticated = check_password_hash(user.password, password)
    if not authenticated:
        raise AuthenticationException


# ===================================================
# Functions to convert model entities to dictionaries
# ===================================================

def user_to_dict(user: User):
    user_dict = {
        'username': user.user_name,
        'password': user.password
    }
    return user_dict


def get_user_reviews(username):
    user = memory.memory_instance.get_user(username)
    return user.reviews
