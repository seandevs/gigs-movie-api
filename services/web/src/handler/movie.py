from flask_restful import Resource

from src.presenter.movie import MovieView

class MovieHandler(Resource):

    def __init__(self, **kwargs):
        self.service = kwargs['service']

    def get(self, movie_id):
        movie = self.service.get(movie_id)

        if not movie:
            return None

        movie_view = MovieView(
                movie_id,
                movie.name,
                movie.release_date,
                movie.imdb_rating,
                movie.runtime
            )

        return movie_view.json()
