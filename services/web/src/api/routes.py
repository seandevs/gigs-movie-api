from flask_restful import Resource

from . import api
from src.handler.movie import MovieHandler
from src.usecase.movie.service import MovieService
from src.repository.movie_repository import MovieRepository

"""
Instantiate Movies
"""

# movie repository
movie_rep = MovieRepository()

# movie service
movie_service = MovieService(movie_rep)

"""
API Endpoints
"""


api.add_resource(
        MovieHandler,
        '/movies/<int:movie_id>',
        resource_class_kwargs={'service': movie_service}
    )
