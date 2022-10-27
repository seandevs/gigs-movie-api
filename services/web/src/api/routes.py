from src.handler.movie import MovieHandler
from src.usecase.movie.service import MovieService
from src.repository.movie_repository import MovieRepository

from src.handler.showtime import ShowTimeHandler
from src.usecase.showtime.service import ShowTimeService
from src.repository.showtime_repository import ShowTimeRepository

from src.handler.imdb_movie import IMDBMovieHandler
from src.usecase.imdb_movie.service import IMDBMovieService
from src.repository.imdb_movie_repository import IMDBMovieRepository

from . import api


# movie repository
movie_rep = MovieRepository()

# movie service
movie_service = MovieService(movie_rep)

# showtime repository
showtime_rep = ShowTimeRepository()

# showtime service
showtime_service = ShowTimeService(showtime_rep)

# imdb repository
imdb_movie_rep = IMDBMovieRepository()

# imdb service
imdb_movie_service = IMDBMovieService(imdb_movie_rep)

api.add_resource(
        MovieHandler,
        '/movies/<int:movie_id>',
        resource_class_kwargs={'service': movie_service}
    )

api.add_resource(
        ShowTimeHandler,
        '/movies/<int:movie_id>/schedule',
        resource_class_kwargs={'service': showtime_service}
    )

api.add_resource(
        IMDBMovieHandler,
        '/imdb_movies/<string:imdb_movie_id>',
        resource_class_kwargs={'service': imdb_movie_service}
        )
