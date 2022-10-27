from src.handler.movie import MovieHandler
from src.usecase.movie.service import MovieService
from src.repository.movie_repository import MovieRepository

from src.handler.showtime import ShowTimeHandler
from src.usecase.showtime.service import ShowTimeService
from src.repository.showtime_repository import ShowTimeRepository

from . import api


# movie repository
movie_rep = MovieRepository()

# movie service
movie_service = MovieService(movie_rep)

# showtime repository
showtime_rep = ShowTimeRepository()

showtime_service = ShowTimeService(showtime_rep)

api.add_resource(
        MovieHandler,
        '/movies/<int:movie_id>',
        resource_class_kwargs={'service': movie_service}
    )

api.add_resource(
        ShowTimeHandler,
        '/movies/schedule/<int:movie_id>',
        resource_class_kwargs={'service': showtime_service}
    )
