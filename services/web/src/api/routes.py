from src.handler.movie import MovieHandler
from src.usecase.movie.service import MovieService
from src.repository.movie_repository import MovieRepository
from . import api


# movie repository
movie_rep = MovieRepository()

# movie service
movie_service = MovieService(movie_rep)

api.add_resource(
        MovieHandler,
        '/movies/<int:movie_id>',
        resource_class_kwargs={'service': movie_service}
    )
