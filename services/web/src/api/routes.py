from flask_restful import Resource

from . import api
from handler.movie import MovieHandler
from usecase.movie.service import MovieService
from repository.movie_repository import MovieRepository

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
        '/movie/<int:movie_id>',
        resource_class_kwargs={'service': movie_service}
    )
