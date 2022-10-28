from src.handler.movie import MovieHandler
from src.usecase.movie.service import MovieService
from src.repository.movie_repository import MovieRepository

from src.handler.showtime import ShowTimeHandler
from src.usecase.showtime.service import ShowTimeService
from src.repository.showtime_repository import ShowTimeRepository

from src.handler.imdb_movie import IMDBMovieHandler
from src.usecase.imdb_movie.service import IMDBMovieService
from src.repository.imdb_movie_repository import IMDBMovieRepository

from src.handler.rating import RatingHandler
from src.usecase.rating.service import RatingService
from src.repository.rating_repository import RatingRepository

from . import api


# movie
movie_rep = MovieRepository()
movie_service = MovieService(movie_rep)

# showtime
showtime_rep = ShowTimeRepository()
showtime_service = ShowTimeService(showtime_rep)

# imdb
imdb_movie_rep = IMDBMovieRepository()
imdb_movie_service = IMDBMovieService(imdb_movie_rep)

# rating
rating_rep = RatingRepository()
rating_service = RatingService(rating_rep)

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

api.add_resource(
        RatingHandler,
        '/movies/<int:movie_id>/rating',
        resource_class_kwargs={'service': rating_service}
    )
