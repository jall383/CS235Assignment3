import os
from flask import Flask, session
import Movie.adapters.data.memory as memory
from Movie.adapters.data import memory, database_repository
from Movie.adapters.data.orm import metadata, map_model_to_tables
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.pool import NullPool


def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')
    data_path = os.path.join('Movie', 'adapters', 'data')

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    memory.memory_instance = memory.Memory_Repository()

    session_factory = sessionmaker(autocommit=False, autoflush=True, bind=database_engine)

    memory.memory_instance = database_repository.SqlAlchemyRepository(session_factory)

    # Build the application - these steps require an application context.
    with app.app_context():
        # Register blueprints.
        from .Home import home
        app.register_blueprint(home.home_blueprint)

        from .movie import mov
        app.register_blueprint(mov.mov_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

        from .utilities import utilities
        app.register_blueprint(utilities.utilities_blueprint)

    return app
