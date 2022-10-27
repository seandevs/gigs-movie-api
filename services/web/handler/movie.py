from flask_restful import Resource

from presenter.movie import MovieView

class MovieHandler(Resource):

    def __init__(self, **kwargs):
        self.service = kwargs['service']

    def get(self, movie_id):
        movie = self.service.get(movie_id)

        if not movie:
            return None

        movie_view = MovieView(
                movie_id,
                movie.get('name'),
                movie.get('release_date'),
                movie.get('imdb_rating'),
                movie.get('runtime')
            )

        return movie_view.json()

