import os
import pytest
from Movie import create_app
from Movie.adapters.data import memory




@pytest.fixture
def in_memory_repo():
    repo = memory.memory_instance
    repo.Memory_Repository()
    return repo


@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,                                # Set to True during testing.
        'WTF_CSRF_ENABLED': False                       # test_client will not send a CSRF token, so disable validation.
    })
    return my_app.test_client()